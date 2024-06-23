# create_books_and_reviews.py

import random
from app.models import Book, Review
book_count = Book.objects.count()
print(f"Book count-----------------------: {book_count}")

book_names = [
    "The Silent Patient",
    "Where the Crawdads Sing",
    "The Night Circus",
    "The Alchemist",
    "The Great Alone",
    "The Immortalists",
    "Little Fires Everywhere",
    "The Light We Lost",
    "The Goldfinch",
    "The Book Thief",
    "The Road",
    "Big Little Lies",
    "The Help",
    "Life of Pi",
    "The Kite Runner",
    "A Thousand Splendid Suns",
    "American Dirt",
    "The Giver of Stars",
    "The Nightingale",
    "The Tattooist of Auschwitz",
    "The Girl on the Train",
    "Gone Girl",
    "Eleanor Oliphant Is Completely Fine",
    "The Woman in the Window",
    "All the Light We Cannot See",
    "The Outsider",
    "The Shack",
    "Water for Elephants",
    "Me Before You",
    "The Martian",
    "The Silent Corner",
    "The Institute",
    "Before We Were Strangers",
    "The Shadow of the Wind",
    "The Girl with the Dragon Tattoo",
    "Sharp Objects",
    "The Silent Corner",
    "The Institute",
    "The Silent Patient",
    "Where the Crawdads Sing",
    "The Night Circus",
    "The Alchemist",
    "The Great Alone",
    "The Immortalists",
    "Little Fires Everywhere",
    "The Light We Lost",
    "The Goldfinch",
    "The Book Thief",
    "The Road"
]

author_names = [
    "Alex Michaelides",
    "Delia Owens",
    "Erin Morgenstern",
    "Paulo Coelho",
    "Kristin Hannah",
    "Chloe Benjamin",
    "Celeste Ng",
    "Jill Santopolo",
    "Donna Tartt",
    "Markus Zusak",
    "Cormac McCarthy",
    "Liane Moriarty",
    "Kathryn Stockett",
    "Yann Martel",
    "Khaled Hosseini",
    "Khaled Hosseini",
    "Jeanine Cummins",
    "Jojo Moyes",
    "Kristin Hannah",
    "Heather Morris",
    "Paula Hawkins",
    "Gillian Flynn",
    "Gail Honeyman",
    "A.J. Finn",
    "Anthony Doerr",
    "Stephen King",
    "William P. Young",
    "Sara Gruen",
    "Jojo Moyes",
    "Andy Weir",
    "Dean Koontz",
    "Stephen King",
    "Renée Carlino",
    "Carlos Ruiz Zafón",
    "Stieg Larsson",
    "Gillian Flynn",
    "Dean Koontz",
    "Stephen King",
    "Alex Michaelides",
    "Delia Owens",
    "Erin Morgenstern",
    "Paulo Coelho",
    "Kristin Hannah",
    "Chloe Benjamin",
    "Celeste Ng",
    "Jill Santopolo",
    "Donna Tartt",
    "Markus Zusak",
    "Cormac McCarthy"
]

genres = [
    "Fiction",
    "Non-Fiction",
    "Mystery",
    "Fantasy",
    "Science Fiction",
    "Romance",
    "Thriller",
    "Historical Fiction",
    "Biography",
    "Self-Help"
]

if book_count == 0:
    for i in range(1, 101):
        random_book_id = random.randint(0, 40)
        genre_ranom_id = random.randint(0, 8)
        random_author_id = random.randint(0, 40)
        book = Book.objects.create(
            title=book_names[random_book_id],
            author=author_names[random_author_id],
            description=f"This is the description of Book {i}.",
            publisher=f"Publisher {i}",
            genre=genres[genre_ranom_id],
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
