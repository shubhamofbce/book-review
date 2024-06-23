from rest_framework import filters
from django_filters import rest_framework as django_filters
from app.models import Book



class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author': ['exact', 'icontains'],
            'genre': ['exact', 'icontains']
        }