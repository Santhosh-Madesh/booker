from django import forms
from .models import Slot, Booking

class SlotModelForm(forms.ModelForm):
    class Meta:
        model = Slot
        fields = '__all__'

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user', 'slot', 'status']