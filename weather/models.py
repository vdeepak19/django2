from django.db import models

# Create your models here.
# weather/models.py

from django.db import models

class WeatherReport(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    weather_description = models.CharField(max_length=200)
