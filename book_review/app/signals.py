# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review

@receiver(post_save, sender=Review)
def handle_review_creation(sender, instance, created, **kwargs):
    if created:
        book = instance.book
        book.total_reviews += 1
        book.average_rating = ((book.average_rating * (book.total_reviews - 1)) + instance.rating) / book.total_reviews
        book.save()
