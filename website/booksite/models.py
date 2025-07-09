from django.db import models
from django.contrib.auth.models import User


class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()

class DailyLimit(models.Model):
    date = models.DateField(unique=True)
    limit = models.PositiveIntegerField(default=10)
    counter = models.PositiveIntegerField(default=0)