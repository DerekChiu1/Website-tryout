from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hi, this is from index")

def login(request):
    return HttpResponse("Hi, this is from login")

def birthday(request, name):
    return HttpResponse(f"Happy birthday {name}!")




