# tests/libros/test_views.py

import pytest
from app.libros.models import Libros


@pytest.mark.django_db
def test_add_book(client):

    # Given
    libros = Libros.objects.all()
    assert len(libros) == 0

    # When
    resp = client.post(
        "/api/libros/",
        {
            "title": "El fin de la eternidad",
            "genre": "Ciencia Ficción",
            "author": "Isaac Asimov",
            "year": "1955",
        },
        content_type="application/json"
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
    resp = client.get(f"/api/libros/{libro.id}/")

    # Then
    assert resp.status_code == 200
    assert resp.data["title"] == "El fin de la eternidad"


@pytest.mark.django_db
def test_get_single_book_incorrect_id(client):

    # When
    resp = client.get(f"/api/libros/-1/")

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
    resp = client.get(f"/api/libros/")

    # Then
    assert resp.status_code == 200
    assert resp.data[0]["title"] == libro_1.title
    assert resp.data[1]["title"] == libro_2.title

