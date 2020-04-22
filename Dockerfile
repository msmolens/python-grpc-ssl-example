# Dockerfile for Python gRPC SSL Example.
#
# The base stage defines the path to the virtual environment.
# The build stage installs the build dependencies.
# The main stage installs the runtime dependencies.

#
# Base stage
#

# Base Python image version
ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

# Path to virtual environment
ENV VIRTUAL_ENV=/opt/venv

# Disable Python output buffering
ENV PYTHONUNBUFFERED=1

#
# Builder stage
#

FROM base as builder

# Path to virtual environment
ENV VIRTUAL_ENV=/opt/venv

# Install build dependencies
RUN apk add --no-cache --update \
    build-base \
    linux-headers

# Create virtual environment owned by guest user
RUN python -m venv $VIRTUAL_ENV && \
    chown -R guest $VIRTUAL_ENV

# Switch to guest user
USER guest

# Install packages into virtual environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN pip install -U pip && \
    pip install -r requirements.txt

#
# Main stage
#

FROM base

# Install runtime dependencies
RUN apk add --no-cache --update \
    libstdc++

# Switch to guest user
USER guest

# Copy virtual environment from builder stage
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Copy application files
COPY . /opt/app

# Activate virtual environment
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

CMD [ "python", "/opt/app/shopping_list_server.py" ]
