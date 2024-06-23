#!/bin/sh

# entrypoint.sh
python manage.py migrate
python manage.py shell < scripts/add_books_and_reviews.py
python manage.py runserver 0.0.0.0:8005