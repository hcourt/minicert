#!/bin/sh
env
echo "Making migrations..."
python manage.py makemigrations app --settings=minicert.settings."${CONFIG_ENV}"

echo "Executing migrations..."
python manage.py migrate --settings=minicert.settings."${CONFIG_ENV}"

echo "Running server..."
python manage.py runserver 0.0.0.0:8000 --settings=minicert.settings."${CONFIG_ENV}"
