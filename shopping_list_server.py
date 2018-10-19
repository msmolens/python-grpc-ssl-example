#!/usr/bin/env python

"""Shopping list gRPC server."""

from concurrent import futures

from shopping_list_service import ShoppingListService

import click
import grpc
import signal
import sys

import shopping_list_pb2_grpc


def read_chain_pair(private_key, certificates):
    """
    Read private key and certificates from files.
    Return (private key, certificates) chain pair.
    """
    with open(private_key, 'rb') as f:
        private_key = f.read()
    with open(certificates, 'rb') as f:
        certificates = f.read()
    return (private_key, certificates)


@click.command()
@click.option('--port', default=8443, help='Port to listen on')
@click.option('--use-tls/--no-use-tls', default=True, help='Use transport layer security (TLS)')
@click.option('--private-key', default='server.key', help='Private key file')
@click.option('--certificates', default='server.crt', help='Certificate file')
def main(port, use_tls, private_key, certificates):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    shopping_list_pb2_grpc.add_ShoppingListServiceServicer_to_server(ShoppingListService(), server)

    if use_tls:
        try:
            chain_pair = read_chain_pair(private_key, certificates)
        except IOError as e:
            print('Failed to read chain pair: {}'.format(e))
            sys.exit(1)

        server_credentials = grpc.ssl_server_credentials([chain_pair])
        server.add_secure_port('[::]:{}'.format(port), server_credentials)
    else:
        server.add_insecure_port('[::]:{}'.format(port))

    server.start()

    try:
        while True:
            signal.pause()
    except KeyboardInterrupt:
        pass

    server.stop(0)


if __name__ == '__main__':
    main()
