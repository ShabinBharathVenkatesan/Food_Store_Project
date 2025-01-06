# In Dish_App/models.py

from django.db import models

class Dish(models.Model):
    dish_name = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    chef = models.ForeignKey('Chef_App.Chef', on_delete=models.CASCADE)  # Correctly reference Chef

    def __str__(self):
        return self.dish_name
