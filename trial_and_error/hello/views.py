from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Where views are created for the hello app

def home(requests):
    return render(requests, 'hello/home.html', {}) # Be carefull with path here, dont need hello/templates/hel..
