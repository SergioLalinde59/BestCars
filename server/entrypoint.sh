#!/bin/sh

# Make migrations and migrate the database.
echo "Making migrations and migrating the database. "
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput
.\djangoenv\Scripts\activate.ps1
python manage.py runserver 127.0.0.1:8000
exec "$@"

