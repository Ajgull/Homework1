from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Sport(request):
    return HttpResponse('Воллейбол')

def Country(request):
    return HttpResponse('Россия')

def Town(requset):
    return HttpResponse('Уфа')