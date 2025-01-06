# Dish_App/serializers.py

from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'dish_name', 'rating', 'chef']  # Include all fields you want to serialize
