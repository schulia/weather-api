from django.shortcuts import render
from .models import Weather
from rest_framework import generics
from .serializers import WeatherSerializer

# Create your views here.
class WeatherListApi(generics.ListCreateAPIView):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer

  def get_queryset(self):
    queryset = Weather.objects.all()
    city = self.request.query_params.get('city')
    date = self.request.query_params.get('date')
    sort = self.request.query_params.get('sort')
    if city is not None: 
      if ',' in city:
        cities = city.split(',')
        capitalized_cities = list(map(lambda city: city.capitalize(), cities))
        queryset = Weather.objects.filter(city__in=capitalized_cities)
      else:
        queryset = queryset.filter(city = city.capitalize())

    if date is not None:
      queryset = queryset.filter(date = date)

    if sort is not None:
      if '-' in sort:
        queryset = queryset.order_by('-date', 'id')
      else:
        queryset = queryset.order_by('date', 'id')
        
    return queryset

class WeatherByIdView(generics.RetrieveAPIView):
  serializer_class = WeatherSerializer

  def get_queryset(self):
    id = self.kwargs['pk']
    return Weather.objects.filter(id=id)