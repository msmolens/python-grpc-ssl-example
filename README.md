# Python gRPC SSL Example

[![CircleCI](https://circleci.com/gh/msmolens/python-grpc-ssl-example.svg?style=shield)](https://circleci.com/gh/msmolens/python-grpc-ssl-example)

[gRPC](https://grpc.io/) client/server example in Python including SSL support.

The example service implements a simple shopping list back end. Clients can
perform the following operations:
- Create a shopping list with a name and description.
- Update a shopping list's name and description.
- Delete a shopping list.
- List available shopping lists, optionally filtering by name. Both unary and
  server streaming methods are demonstrated.
- Add an item to a shopping list.
- Remove an item from a shopping list.
- Check or uncheck an item.
- List items on a shopping list, optionally filtering by name. Both unary and
  server streaming methods are demonstrated.

See https://grpc.io/docs/quickstart/python.html for documentation on using
gRPC in Python.

## Usage

### Prerequisites

Install the required runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

Alternatively, if using Docker, install:
- [Docker Engine](https://docs.docker.com/engine/) >= 18.02.0
- [Docker Compose](https://docs.docker.com/compose/) >= 18.02.0

## Testing

The [test](test) directory contains unit tests runnable with
[pytest](https://pytest.org).

To automatically test on multiple versions of Python, install and run
[`tox`](https://tox.readthedocs.io/). [Flake8](http://flake8.pycqa.org/) is used
to check the code style.

## Usage

### Run the server

Run the server with the following command:

```bash
./shopping_list_server.py --no-use-tls
```

Alternatively, if using Docker, run:
```bash
docker-compose up -d --build
```

Later, stop the Docker container with:
```bash
docker-compose down
```

### Run the test client

A test client is provided that exercises some methods of the server. Run the
test client with the following command:

```bash
./shopping_list_test_client.py --no-use-tls
```

Note that SSL support is enabled by default; the `--no-use-tls` option disables
it.

Alternatively, if using Docker, run:
```bash
docker run -it --rm \
    --network container:python-grpc-ssl-example-server \
    python-grpc-ssl-example:latest \
    /opt/app/shopping_list_test_client.py --no-use-tls
```

### Additional options

Pass the `--help` argument when running the client and server to see additional
options, including those for host and port.

## Development

### Prerequisites

Install the required development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

### Generated code

The [protos](protos) directory contains the message and service definitions.
When the definitions change, run `generate_stubs.py` update the generated code.
The generated files are named like `<name>_pb2.py` and `<name>_pb2_grpc.py`
where `<name>` is the name of the `.proto` file.

### SSL

gRPC uses SSL for authentication and encryption of data transferred between the
server and client. A self-signed SSL certificate is sufficient for testing and
development. Generate such a certificate by running following command and
answering the questions:

```bash
openssl req -newkey rsa:2048 -nodes -keyout server.key -sha256 -x509 -days 3650 -out server.crt
```

Make sure to set the Common Name (CN) as the host name of the server, or
`localhost` if testing locally. When running the test client, specify the server
host name with the `--host` argument.
