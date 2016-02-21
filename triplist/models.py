from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TripList(models.Model):
    available_drivers = models.IntegerField(max_length=255)
    seats_available = models.CharField(max_length=255) # Probably not going to stay as a charfield
    destinations = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    misc_descriptions = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)
