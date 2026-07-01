from django.db import models

class Entry(models.Model):
    """ An entry in our story or topic """
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        """ Return a string representation of the model """
        return self.text
    
