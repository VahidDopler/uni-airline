from django.db import models
import hashlib
from flightmanager.models import Flight
from usermanagement.models import normal_user


class Ticket(models.Model):
    user = models.ForeignKey(normal_user, on_delete=models.CASCADE, related_name="tickets")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="tickets")
    seat_number = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ticket {self.id} for {self.user} on flight {self.flight}"

# Create your models here.
