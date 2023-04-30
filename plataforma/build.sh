#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install
pip install --upgrade pip
pip install python-dotenv
#pip install -r requirements.txt

#python3 manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
#python manage.py runserver
