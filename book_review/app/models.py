from django.db import models


# Add logic for total reviews and average rating
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    publisher = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=30, blank=True)
    average_rating = models.FloatField(default=0.0)
    total_reviews = models.IntegerField(default=0)
    cover_image_url = models.URLField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'app'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book.title

    class Meta:
        app_label = 'app'
