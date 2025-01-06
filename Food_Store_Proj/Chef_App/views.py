from django.shortcuts import render

# Create your views here.
# Chef_App/views.py



# Chef_App/views.py

from rest_framework.viewsets import ModelViewSet
from .models import Chef
from .serializers import ChefSerializer

class ChefViewSet(ModelViewSet):
    queryset = Chef.objects.all()  # Queryset to retrieve all chef instances
    serializer_class = ChefSerializer  # Serializer to convert model instances to JSON and vice versa
