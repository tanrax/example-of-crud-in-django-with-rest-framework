# app/libros/views.py

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LibroSerializer
from .models import Libros


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


class LibrosList(APIView):

    def get(self, request, format=None):
        libros = Libros.objects.all().order_by('created_at')
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibrosDetails(APIView):

    def get(self, request, pk, format=None):
        libro = Libros.objects.filter(pk=pk).first()
        serializer = LibroSerializer(libro)
        if libro:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

