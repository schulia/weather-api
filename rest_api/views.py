from django.shortcuts import render
from .models import Weather
from rest_framework import generics
from .serializers import WeatherSerializer

# Create your views here.
class WeatherListApi(generics.ListCreateAPIView):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer