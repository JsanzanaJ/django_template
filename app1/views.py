from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mi_vista(request):
    return HttpResponse("¡Hola, mundo!")
