from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import introduction # import the class

# Create your views here.
# Where views are created for the hello app
# Used to link models to tmplates

def home(request):
    people = introduction.objects.all()
    return render(request, 'hello/home.html', {'people': people }) # Be carefull with path here, dont need hello/templates/hel..
