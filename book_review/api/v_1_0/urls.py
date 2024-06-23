from django.urls import include, re_path, path
from api.v_1_0 import views
from rest_framework.routers import DefaultRouter

# attach a new viewset for book review book/:id/reviews

router = DefaultRouter()
router.register(r'books', views.BooksViewSet, "books")

urlpatterns = [
    path('book/<int:bookid>/review/', views.BookReviewAPIView.as_view(), name='book-review-api'),
    re_path(r'^', include(router.urls)),
    
]