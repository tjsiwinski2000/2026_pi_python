""" Defines URL patterns for hangman app. """

from django.urls import path
from . import views

app_name = 'hangman'

urlpatterns = [
    # Main Form
    path ('', views.index, name ='index'), 
]