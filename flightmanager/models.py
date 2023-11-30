from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField

from usermanagement.models import normal_user


class Country(models.Model):
    country = CountryField(null=True)

    def __str__(self):
        return f"{self.country.name}"

    class Meta:
        verbose_name_plural = "Countries"


class Airport(models.Model):
    name = models.CharField(max_length=55)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="airports")

    def __str__(self):
        return f"{self.name} ({self.country})"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    departure = models.DateTimeField(auto_now=True)  # save it every time, allowing to update the hour.
    arrival = models.DateTimeField(auto_now=True)
    airplane = models.ForeignKey('Airplane', on_delete=models.SET_NULL, null=True, related_name="flights", blank=True)

    def __str__(self):
        return f"A flight from {self.origin} to {self.destination}"


class Airplane(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(default=40)

    def __str__(self):
        return f"{self.brand} {self.model}"

# Create your models here.
