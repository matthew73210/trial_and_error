from django.urls import path
from . import views

# Here we route the different urls to the views in the app.
# Not to be confused with the urls.py in the project folder

urlpatterns = [
    path("", views.home, name="home"), # here we have assigned views.home to root url
]
