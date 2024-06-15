#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

apt-get update
apt-get -y install alembic

# Run Alembic migrations
echo "Running Alembic migrations"
cd db_connector/
alembic upgrade head
cd ../

# Start the gRPC service
echo "Starting kafka_listener server"
exec "$@"