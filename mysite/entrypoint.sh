#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Start the server
echo "Starting server..."
exec "$@"