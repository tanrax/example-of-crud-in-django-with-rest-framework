# tests/Library/test_model.py

import pytest
from app.library.models import Book


@pytest.mark.django_db
def test_book_model():

    ## Given
    book = Book(
        title="The foundation",
        genre="Science fiction",
        year="1951",
        author="Isaac Asimov",
    )
    book.save()

    ## When

    ## Then
    assert book.title == "The foundation"
    assert book.genre == "Science fiction"
    assert book.year == "1951"
    assert book.author == "Isaac Asimov"
    assert book.created_at
    assert book.updated_at
    assert str(book) == book.title
