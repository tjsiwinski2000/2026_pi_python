from django.shortcuts import render
from .models import Animal

def mosaic(request):
    animals = Animal.objects.all().order_by("name")
    return render(request, "animals/mosaic.html", {"animals": animals})