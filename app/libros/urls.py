# app/libros/urls.py

from django.urls import path
from app.libros.views import ping, LibrosList


urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/libros/", LibrosList.as_view()),
]