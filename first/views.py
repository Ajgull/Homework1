from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def RecFirst(request):
    return HttpResponse('Добрый вечер')

def RecSecond(request):
    return HttpResponse('Второй запрос')

def RecThird(request):
    return HttpResponse('Третий запрос')

def RecForth(request):
    return HttpResponse('Дз №2')