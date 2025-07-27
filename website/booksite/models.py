from django.db import models
from django.contrib.auth.models import User
import datetime

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    start_time = models.IntegerField(blank=False)
    end_time = models.IntegerField(blank=False)
    date = models.DateField(blank=False, default=datetime.date.today())
    duration = models.PositiveSmallIntegerField(default=1)
    status = models.BooleanField(null=False, default=False)

    def __str__(self):
        return str(self.start_time)

class DailyLimit(models.Model):
    date = models.DateField(unique=True)
    limit = models.PositiveIntegerField(default=7)
    counter = models.PositiveIntegerField(default=1)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.FileField(default='default.jpg', upload_to='profile_pics')
    username = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    bio = models.CharField(max_length=500, blank=True, null=True)
    contact = models.PositiveIntegerField(default=0)

    # later work on gender choice field