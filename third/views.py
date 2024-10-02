from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Hobby(request):
    return HttpResponse('Programming')

def Univercity(request):
    return HttpResponse('USATU')

def Work(request):
    return  HttpResponse('Hope IT Code')