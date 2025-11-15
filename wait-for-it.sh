#!/bin/bash

# Wait for PostgreSQL with timeout (max 60 seconds)
echo "Waiting for PostgreSQL..."
counter=0
max_wait=5

until python -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(('db', 5432))
    s.close()
    exit(0)
except:
    exit(1)
"; do
    counter=$((counter + 1))
    echo "PostgreSQL not ready... waiting ($counter/$max_wait)"
    sleep 2
    
    if [ $counter -ge $max_wait ]; then
        echo "Warning: PostgreSQL not available after 60 seconds, continuing anyway..."
        break
    fi
done

echo "PostgreSQL is ready!"

# Wait for Redis with timeout
echo "Waiting for Redis..."
counter=0

until python -c "
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(('cache', 6379))
    s.close()
    exit(0)
except:
    exit(1)
"; do
    counter=$((counter + 1))
    echo "Redis not ready... waiting ($counter/$max_wait)"
    sleep 2
    
    if [ $counter -ge $max_wait ]; then
        echo "Warning: Redis not available after 60 seconds, continuing anyway..."
        break
    fi
done

echo "Redis is ready!"

# Apply migrations and collect static
echo "Applying database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Populate recommendation engine
echo "Populating recommendation engine..."
python manage.py populate_recommendations

# Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn myshop.wsgi:application --bind 0.0.0.0:8000 --workers 3