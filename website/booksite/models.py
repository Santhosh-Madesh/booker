from django.db import models
from django.contrib.auth.models import User
import datetime

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.TimeField(blank=False, default=datetime.time(9,0,0))
    end_time = models.TimeField(blank=False, default=datetime.time(9,0,0))
    date = models.DateField(blank=False, default=datetime.date.today())
    status = models.BooleanField(null=False, default=False)

class DailyLimit(models.Model):
    date = models.DateField(unique=True)
    limit = models.PositiveIntegerField(default=10)
    counter = models.PositiveIntegerField(default=1)

# Change of plans. I have now made it such that there is no slot model but i am integrating that model's functionality along with the booking model