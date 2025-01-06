# Dish_App/views.py

from rest_framework.viewsets import ModelViewSet
from .models import Dish
from .serializers import DishSerializer

class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()  # Queryset to retrieve all dish instances
    serializer_class = DishSerializer  # Serializer to convert model instances to JSON and vice versa
