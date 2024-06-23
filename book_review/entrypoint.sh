#!/bin/sh

# entrypoint.sh
python manage.py migrate
python manage.py shell < scripts/add_books_and_reviews.py
gunicorn book_review.wsgi:application --bind "0.0.0.0:8000"