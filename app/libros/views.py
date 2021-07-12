# app/libros/views.py

from django.http import JsonResponse
from rest_framework.views import APIView # nuevo
from rest_framework.response import Response # nuevo
from rest_framework import status # nuevo
from .serializers import LibroSerializer # nuevo


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


class LibrosList(APIView):

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)