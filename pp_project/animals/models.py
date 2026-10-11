from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="animals/")
    caption = models.CharField(max_length=200, blank=True)
    funfacts = models.TextField(blank=True) # one fact per line
    AOD = models.BooleanField(default=False) # True = eligible
    
    def __str__(self):
        return self.name
    
    def facts(self):
        return self.funfacts.splitlines()
