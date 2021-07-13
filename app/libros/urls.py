# app/libros/urls.py

from django.urls import path
from app.libros.views import *


urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/libros/", LibrosList.as_view(), name="libros_list"),
    path("api/libros/<int:pk>/", LibrosDetails.as_view(), name="libros_details"),
]
