from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hola mundo.")

def greeting(request, name):
    return HttpResponse(f"Hello, {name}!")
