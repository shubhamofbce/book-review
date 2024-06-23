# Generated by Django 5.0.6 on 2024-06-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('genre', models.CharField(blank=True, max_length=50)),
                ('isbn', models.CharField(blank=True, max_length=20, unique=True)),
                ('page_count', models.IntegerField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=30)),
                ('average_rating', models.FloatField(default=0.0)),
                ('total_reviews', models.IntegerField(default=0)),
                ('cover_image_url', models.URLField(blank=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
