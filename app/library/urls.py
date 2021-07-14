# app/Library/urls.py

from django.urls import path
from app.library.views import ping, BookList, BookDetails


urlpatterns = [
    path("ping/", ping, name="ping"),
    path("api/book/", BookList.as_view(), name="book_list"),
    path("api/book/<int:pk>/", BookDetails.as_view(), name="book_details"),
]
