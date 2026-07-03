""" Defines URL patterns for pi_python."""

from django.urls import path

from . import views

app_name = 'pi_python'

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/', views.index, name='temp'),
]
