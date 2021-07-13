# app/libros/serializers.py

from rest_framework import serializers
from .models import Libros


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libros
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
