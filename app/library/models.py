# app/Library/models.py

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
