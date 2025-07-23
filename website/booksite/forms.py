from tokenize import Number

from django import forms
from django.forms import NumberInput

from .models import Booking, Profile
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
    format='%H'

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user', 'status', 'duration']
        widgets = {
            'start_time':NumberInput(),
            'end_time':NumberInput(),
            'date':DateInput(),
        }

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(),
        }

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            "pfp":forms.FileInput(),
            "age":forms.NumberInput(),
            "bio":forms.Textarea(),
        }

class BookDateForm(forms.Form):
    date = forms.DateField(widget=DateInput())