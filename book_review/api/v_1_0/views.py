from rest_framework import viewsets, permissions, filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from api.v_1_0.serializers import BooksSerializer, ReviewsSerializer, BookReviewSerializer
from api.v_1_0.filters import BookFilter
from app.models import Book, Review


class CustomPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

def homePageView(request):
    return HttpResponse("Welcome to ai video app!")

class GenericModelViewset(viewsets.ModelViewSet):
    def custom_filter_queryset(self, queryset):
        return queryset.filter(maintainer=self.request.user).order_by('id')

    def get_serializer_context(self):
        return {
            "user": self.request.user,
        }


class BooksViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = BooksSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter)
    filterset_class = BookFilter
    search_fields = ['name']
    ordering_fields = ['created', 'updated', 'name', 'author']
    pagination_class = CustomPagination
    queryset = Book.objects.all()


class BookReviewAPIView(APIView):
    def get(self, request, bookid):
        try:
            book = Book.objects.get(pk=bookid)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        reviews = Review.objects.filter(book=book)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(reviews, request)
        data = {
            "book": bookid,
            "total_reviews": book.total_reviews,
            "average_rating": book.average_rating,
            "reviews": result_page
        }
        serializer = BookReviewSerializer(data)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, bookid):
        try:
            book = Book.objects.get(pk=bookid)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        request.data['book'] = bookid
        serializer = ReviewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(book=book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
