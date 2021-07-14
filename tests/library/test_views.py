# tests/Library/test_views.py

import pytest
from app.library.models import Book
from django.urls import reverse


@pytest.mark.django_db
def test_add_book(client):

    # Given
    book = Book.objects.all()
    assert len(book) == 0

    # When
    resp = client.post(
        reverse("book_list"),
        {
            "title": "The End of Eternity",
            "country": "eeuu",
            "author": "Isaac Asimov",
            "year": "1955",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 201
    assert resp.data["title"] == "The End of Eternity"

    book = Book.objects.all()
    assert len(book) == 1


@pytest.mark.django_db
def test_get_single_book(client):

    # Given
    book = Book.objects.create(
        title="The End of Eternity",
        country="eeuu",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.get(reverse("book_details", kwargs={"pk": book.id}))

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "The End of Eternity"


@pytest.mark.django_db
def test_get_single_book_incorrect_id(client):

    # When
    resp = client.get(reverse("book_details", kwargs={"pk": 99}))

    # Then
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_books(client, faker):

    # Given
    def create_random_book():
        return Book.objects.create(
            title=faker.name(),
            country=faker.country(),
            author=faker.name_nonbinary(),
            year=faker.year(),
        )

    book_1 = create_random_book()
    book_2 = create_random_book()

    # When
    resp = client.get(reverse("book_list"))

    # Then
    assert resp.status_code == 200
    assert resp.data[0]["title"] == book_1.title
    assert resp.data[1]["title"] == book_2.title


@pytest.mark.django_db
def test_remove_book(client):

    # Given
    book = Book.objects.create(
        title="The End of Eternity",
        country="eeuu",
        author="Isaac Asimov",
        year="1955",
    )
    ## Check exist
    resp_detail = client.get(reverse("book_details", kwargs={"pk": book.id}))
    assert resp_detail.status_code == 200
    assert resp_detail.data["title"] == "The End of Eternity"

    # When
    resp_delete = client.delete(reverse("book_details", kwargs={"pk": book.id}))
    resp_list = client.get(reverse("book_list"))
    rest_new_detail = client.get(reverse("book_details", kwargs={"pk": book.id}))

    # Then
    ## Check status delete
    assert resp_delete.status_code == 200
    ## Check return delete
    assert resp_delete.data["title"] == "The End of Eternity"
    ## Check status list
    assert resp_list.status_code == 200
    ## Check not item list
    assert len(resp_list.data) == 0
    ## Check not exist detail
    assert rest_new_detail.status_code == 404


@pytest.mark.django_db
def test_remove_book_incorrect_id(client):
    # Given
    book = Book.objects.create(
        title="The End of Eternity",
        country="eeuu",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.delete(reverse("book_details", kwargs={"pk": 99}))

    # Then
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_book(client):

    # Given
    book = Book.objects.create(
        title="The End of Eternity",
        country="eeuu",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.put(
        reverse("book_details", kwargs={"pk": book.id}),
        {
            "title": "Dune",
            "country": "eeuu",
            "author": "Frank Herbert",
            "year": "1965",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "Dune"
    assert resp.data["country"] == "eeuu"
    assert resp.data["author"] == "Frank Herbert"
    assert resp.data["year"] == "1965"

    resp_detail = client.get(reverse("book_details", kwargs={"pk": book.id}))
    assert resp_detail.status_code == 200
    assert resp_detail.data["title"] == "Dune"
    assert resp_detail.data["country"] == "eeuu"
    assert resp_detail.data["author"] == "Frank Herbert"
    assert resp_detail.data["year"] == "1965"


@pytest.mark.django_db
def test_update_book_incorrect_id(client):
    resp = client.put(reverse("book_details", kwargs={"pk": 99}))
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_book_invalid_json(client):
    # Given
    book = Book.objects.create(
        title="The End of Eternity",
        country="eeuu",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.put(
        reverse("book_details", kwargs={"pk": book.id}),
        {
            "foo": "Dune",
            "boo": "Sciencie Fiction",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 400
