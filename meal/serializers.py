from rest_framework import serializers
from .models import FoodDB

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDB
        fields = '__all__'