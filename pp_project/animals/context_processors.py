from datetime import date
from .models import Animal

def animal_of_the_day(request):
    animals = list(Animal.objects.filter(AOD=True).order_by("id"))
    if not animals:
        return {"animal_of_the_day": None}
    pick = animals[date.today().toordinal() % len(animals)]
    return {"animal_of_the_day": pick}
