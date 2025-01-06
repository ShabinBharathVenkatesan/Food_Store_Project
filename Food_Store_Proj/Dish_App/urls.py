# Dish_App/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DishViewSet

# Create a router and register our DishViewSet with it.
router = DefaultRouter()
router.register(r'dishes', DishViewSet)  # Registering the viewset with a URL prefix 'dishes'

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
