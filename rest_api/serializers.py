from rest_framework import serializers
from .models import Weather

# Implement your serializers here

class WeatherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Weather
    fields = '__all__'