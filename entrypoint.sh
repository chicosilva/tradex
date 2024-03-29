#!/bin/sh

echo "Waiting for postgres..."

#while ! nc -z db 5432; do
#  sleep 0.1
#done

echo "PostgreSQL started"

#python manage.py flush --no-input
# PGPASSWORD=djangoproject psql --host db --port 5432 --username=code.djangoproject --dbname=code.djangoproject < tracdb/trac.sql
echo "---- Run Migrations ----"
python manage.py migrate
python manage.py collectstatic --no-input --clear
python manage.py runserver 0.0.0.0:8000
exec "$@"