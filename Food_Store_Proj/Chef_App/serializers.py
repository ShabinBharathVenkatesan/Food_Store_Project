# Chef_App/serializers.py

from rest_framework import serializers
from .models import Chef

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ['id', 'full_name', 'age', 'image']  # Include all fields you want to serialize
