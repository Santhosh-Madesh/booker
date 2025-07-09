from django.shortcuts import render
from .forms import SlotModelForm, BookingModelForm

def home(request):
    return render(request, "booksite/index.html")
