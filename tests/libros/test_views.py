# tests/libros/test_views.py

import pytest
from app.libros.models import Libros


@pytest.mark.django_db
def test_add_movie(client):
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