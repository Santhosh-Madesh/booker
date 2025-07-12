from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from .models import Booking, DailyLimit
from .forms import BookingModelForm
from django.contrib import messages
from django.urls import reverse_lazy

def home(request):
    return render(request, "booksite/index.html")

class BookingCreate(CreateView):
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
        obj.save()
        messages.success(self.request, "Slot Booked Successfully!")
        return super().form_valid(form)

    # make the logic such that no two same slot exists
    # logic for the time field
    # say we have two slots with s_time1, e_time1 and s_time2, e_time2.
    # a slot should only be booked if s_time1 is either great or less than e_time2 where the e_time1 should be either great or less than s_time2