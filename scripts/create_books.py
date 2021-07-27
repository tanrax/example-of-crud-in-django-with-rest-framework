from app.library.models import Book
import json

def run():

    print('Working')

    # Delete old books
    Book.objects.all().delete()

    # Read file
    with open("scripts/example_books.json", "r") as file_books:
        books = json.loads(file_books.read())

    # Create books
    for index, book in enumerate(books):
        Book(
            id=index + 1,
            title=book['title'],
            author=book['author'],
            country=book['country'],
            year=book['year'],
        ).save()

    print('Finish!')
