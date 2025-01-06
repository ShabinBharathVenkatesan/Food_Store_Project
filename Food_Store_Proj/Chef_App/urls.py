# Chef_App/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChefViewSet

# Create a router and register our ChefViewSet with it.
router = DefaultRouter()
router.register(r'chefs', ChefViewSet)  # Registering the viewset with a URL prefix 'chefs'

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]
