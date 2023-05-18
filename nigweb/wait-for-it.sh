#!/usr/bin/env bash
python manage.py makemigrations web
python manage.py migrate
python manage.py createsuperuser --noinput