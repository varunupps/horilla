#!/bin/bash

echo "Waiting for database to be ready..."
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
#python3 manage.py createhorillauser --first_name admin --last_name admin --username admin --password admin --email admin@example.com --phone 1234567890

# Load demo data automatically when using Docker
if [ -n "$DOCKER_CONTAINER" ]; then
    echo "Running in Docker container, loading demo data..."
    python3 manage.py loaddemodata --force
fi

# Use Django's development server for auto-reloading during development
python3 manage.py runserver 0.0.0.0:8000
