from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Where views are created for the hello app

def home(requests):
    return HttpResponse("Hello, this is a simmple introduction")
