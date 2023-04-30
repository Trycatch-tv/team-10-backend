#!/usr/bin/env bash
# exit on error
set -o errexit


pip install --upgrade pip
pip install uvicorn
pip install python-dotenv
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate

