from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>OmSaiRam</h1>")

def viewV1(response):
    return HttpResponse("<h1>OmSaiRam V1</h1>")
