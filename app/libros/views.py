from django.http import JsonResponse
from django.http import JsonResponse


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)

def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)