

# Create your models here.
from django.db import models

class Chef(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='chefs/')

    def __str__(self):
        return self.full_name
