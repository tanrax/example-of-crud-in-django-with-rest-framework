# tests/libros/test_views.py

import pytest
from app.libros.models import Libros
from django.urls import reverse


@pytest.mark.django_db
def test_add_book(client):

    # Given
    libros = Libros.objects.all()
    assert len(libros) == 0

    # When
    resp = client.post(
        reverse("libros_list"),
        {
            "title": "El fin de la eternidad",
            "genre": "Ciencia Ficción",
            "author": "Isaac Asimov",
            "year": "1955",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 201
    assert resp.data["title"] == "El fin de la eternidad"

    libros = Libros.objects.all()
    assert len(libros) == 1


@pytest.mark.django_db
def test_get_single_book(client):

    # Given
    libro = Libros.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.get(reverse("libros_details", kwargs={"pk": libro.id}))

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "El fin de la eternidad"


@pytest.mark.django_db
def test_get_single_book_incorrect_id(client):

    # When
    resp = client.get(reverse("libros_details", kwargs={"pk": 99}))

    # Then
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_books(client, faker):

    # Given
    def create_random_book():
        return Libros.objects.create(
            title=faker.name(),
            genre=faker.job(),
            author=faker.name_nonbinary(),
            year=faker.year(),
        )

    libro_1 = create_random_book()
    libro_2 = create_random_book()

    # When
    resp = client.get(reverse("libros_list"))

    # Then
    assert resp.status_code == 200
    assert resp.data[0]["title"] == libro_1.title
    assert resp.data[1]["title"] == libro_2.title


@pytest.mark.django_db
def test_remove_book(client):

    # Given
    libro = Libros.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
    )
    ## Check exist
    resp_detail = client.get(reverse("libros_details", kwargs={"pk": libro.id}))
    assert resp_detail.status_code == 200
    assert resp_detail.data["title"] == "El fin de la eternidad"

    # When
    resp_delete = client.delete(reverse("libros_details", kwargs={"pk": libro.id}))
    resp_list = client.get(reverse("libros_list"))
    rest_new_detail = client.get(reverse("libros_details", kwargs={"pk": libro.id}))

    # Then
    ## Check status delete
    assert resp_delete.status_code == 200
    ## Check return delete
    assert resp_delete.data["title"] == "El fin de la eternidad"
    ## Check status list
    assert resp_list.status_code == 200
    ## Check not item list
    assert len(resp_list.data) == 0
    ## Check not exist detail
    assert rest_new_detail.status_code == 404


@pytest.mark.django_db
def test_remove_book_incorrect_id(client):
    # Given
    libro = Libros.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.delete(reverse("libros_details", kwargs={"pk": 99}))

    # Then
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_book(client):

    # Given
    libro = Libros.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.put(
        reverse("libros_details", kwargs={"pk": libro.id}),
        {
            "title": "Dune",
            "genre": "Ciencia Ficción",
            "author": "Frank Herbert",
            "year": "1965",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "Dune"
    assert resp.data["genre"] == "Ciencia Ficción"
    assert resp.data["author"] == "Frank Herbert"
    assert resp.data["year"] == "1965"

    resp_detail = client.get(reverse("libros_details", kwargs={"pk": libro.id}))
    assert resp_detail.status_code == 200
    assert resp_detail.data["title"] == "Dune"
    assert resp_detail.data["genre"] == "Ciencia Ficción"
    assert resp_detail.data["author"] == "Frank Herbert"
    assert resp_detail.data["year"] == "1965"


@pytest.mark.django_db
def test_update_book_incorrect_id(client):
    resp = client.put(reverse("libros_details", kwargs={"pk": 99}))
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_book_invalid_json(client):
    # Given
    libro = Libros.objects.create(
        title="El fin de la eternidad",
        genre="Ciencia Ficción",
        author="Isaac Asimov",
        year="1955",
    )

    # When
    resp = client.put(
        reverse("libros_details", kwargs={"pk": libro.id}),
        {
            "foo": "Dune",
            "boo": "Ciencia Ficción",
        },
        content_type="application/json",
    )

    # Then
    assert resp.status_code == 400
