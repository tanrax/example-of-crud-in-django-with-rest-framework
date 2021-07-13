# tests/libros/test_create_model.py

import pytest

from app.libros.models import Libros


@pytest.mark.django_db
def test_libros_model():

    ## Given
    # Creamos un nuevo libro en la base de datos
    libro = Libros(
        title="La fundación",
        genre="Ciencia ficción",
        year="1951",
        author="Isaac Asimov",
    )
    libro.save()

    ## When

    ## Then
    assert libro.title == "La fundación"
    assert libro.genre == "Ciencia ficción"
    assert libro.year == "1951"
    assert libro.author == "Isaac Asimov"
    assert libro.created_at
    assert libro.updated_at
    assert str(libro) == libro.title
