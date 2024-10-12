from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Developer. You're at the Axidots homepage.")