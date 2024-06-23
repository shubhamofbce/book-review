# create_books_and_reviews.py

import random
from app.models import Book, Review
book_count = Book.objects.count()
print(f"Book count-----------------------: {book_count}")

if book_count == 0:
    for i in range(1, 101):
        book = Book.objects.create(
            title=f"Book Title {i}",
            author=f"Author {i}",
            description=f"This is the description of Book {i}.",
            publisher=f"Publisher {i}",
            genre=f"Genre {i}",
            isbn=f"978-0-0000-{i:04d}",
            page_count=random.randint(100, 500),
            language="English",
            cover_image_url=f"https://picsum.photos/id/{i}/200/300"
        )

        for j in range(1, 6):
            Review.objects.create(
                book=book,
                comment=f"This is review {j} for Book {i}.",
                rating=random.randint(1, 5)
            )

    print("Books and reviews created successfully.")
