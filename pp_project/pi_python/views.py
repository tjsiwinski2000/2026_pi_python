from django.shortcuts import render
from .get_weather_now import get_weather

def index(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)

def temp(request):
    weather = get_weather('F')
    context = {'weather_report' : weather,'unit' : 'F'}
    return render(request, 'pi_python/index.html', context)
