from rest_framework import serializers
from app.models import Book, Review


class BooksSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    class Meta:
        model = Book
        fields = ('__all__')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Round the average_rating to one decimal place
        if 'average_rating' in representation:
            representation['average_rating'] = round(representation['average_rating'], 1)
        return representation


# TODO: Add more validation to the serializer
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('__all__')
    
    def validate_rating(self, value):
        if value < 0 or value > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5.")
        return value

    def validate_comment(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Comment cannot be empty.")
        return value
    

class BookReviewSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField()
    total_reviews = serializers.IntegerField()
    reviews = ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('average_rating', 'total_reviews', 'reviews')
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'average_rating' in representation:
            representation['average_rating'] = round(representation['average_rating'], 1)
        return representation