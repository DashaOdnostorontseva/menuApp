#!/bin/sh

set -e  # падать при любой ошибке

echo "Apply migrations..."
python manage.py migrate --noinput

echo "Load initial menu data (if not loaded yet)..."
# Если фикстура уже загружена и будут ошибки - не роняем контейнер
python manage.py loaddata initial_menu || echo "Fixture load failed or already loaded, continuing"

echo "Run dev server..."
python manage.py runserver 0.0.0.0:8000
