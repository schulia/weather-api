from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField

class Weather(models.Model):
  date = models.DateField()
  lat = models.DecimalField(max_digits=6, decimal_places=4)
  lon = models.DecimalField(max_digits=7, decimal_places=4)
  city = models.TextField()
  state = models.TextField()
  temperatures =  ArrayField(models.CharField(max_length=50))

  objects = models.Manager()

class Meta:
  def get_absolute_url(self):
     return reverse("weather:city", kwargs={"city": self.city})