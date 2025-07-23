from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Booking, DailyLimit, Profile
from .forms import BookingModelForm, ProfileModelForm, BookDateForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta, date

@login_required
def home(request):
    return render(request, "booksite/index.html")

class BookingCreate(LoginRequiredMixin ,CreateView):
    model = Booking
    form_class = BookingModelForm
    template_name = "booksite/booking.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        date = form.cleaned_data['date']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        if not start_time < end_time:
            messages.warning(self.request, "The End time must be after the Start time")
            return super().form_invalid(form)
        dl = DailyLimit.objects.filter(date=date).first()
        if not dl:
            dl = DailyLimit(date=date)
            dl.save()
        else:
            if dl.counter == dl.limit:
                return HttpResponse("Booking is full!")
            else:
                other_obj = Booking.objects.filter(date=date)
                for data in other_obj:
                    if data.start_time == start_time:
                        messages.warning(self.request, "The slot has already been booked! Try a different one please.")
                        return super().form_invalid(form)
                    else:
                        pass
                dl.counter += 1
                dl.save()
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.duration = 1
        obj.save()
        messages.success(self.request, "Slot Booked Successfully!")
        return super().form_valid(form)

# Code for User Dashboard starts from here....

class UserDashboard(LoginRequiredMixin, ListView):
    template_name = "booksite/dashboard.html"
    context_object_name = "profile"

    def get_queryset(self):
        obj  = Profile.objects.filter(user=self.request.user).first()
        return obj

class UserDashboardCreate(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = "booksite/dashboard_create.html"
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, "Profile created successfully!")
        return super().form_valid(form)

class UserDashboardDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = "booksite/dashboard_delete.html"
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Profile deleted successfully!")
        return super().post(self.request)

    def test_func(self):
        obj = Profile.objects.filter(pk=self.kwargs['pk']).first()
        return obj.user == self.request.user

class UserDashboardUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = "booksite/dashboard_update.html"
    form_class = ProfileModelForm
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Profile updated successfully!")
        return super().post(self.request)

    def test_func(self):
        obj = Profile.objects.filter(pk=self.kwargs['pk']).first()
        return obj.user == self.request.user


def contact(request):
    return render(request, 'booksite/contact.html')

def selectDate(request):
    dates = []
    current_date = date.today()
    dates.append(current_date)
    for i in range(1,7):
        result = current_date + timedelta(days=i)
        dates.append(result)
    return render(request, "booksite/select_date.html", {'dates':dates})

def selectSlot(request, book_date):
    qs = DailyLimit.objects.filter(date=book_date).first()
    if qs and qs.counter >= qs.limit:
        return HttpResponse("Booking is full")
    else:
        slots = []
        start_time = 1
        end_time = 2
        for i in range(1, 10):
            booking_slot = Booking.objects.filter(date=book_date, start_time=start_time, end_time=end_time).first()
            if booking_slot:
                pass
            else:
                slots.append(start_time)
            start_time+=1
            end_time+=1

        return render(request, "booksite/select_slot.html", {"slots":slots, "date":book_date})

def booking(request, book_date ,book_slot):
    dl = DailyLimit.objects.filter(date=book_date).first()
    if dl:
        dl.counter +=1
        dl.save()
    else:
        dl = DailyLimit(date=book_date)
        dl.save()
    book = Booking(date=book_date, start_time=book_slot, end_time=book_slot+1, user=request.user)
    book.save()
    messages.success(request, "Slot successfully booked!")
    return redirect("home")