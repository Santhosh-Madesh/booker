from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.messages.context_processors import messages
from django.contrib import messages

from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "booksite/signup.html"
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        password = form.cleaned_data.get('password')
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        return super().form_valid(form)

class LoginClassView(LoginView):
    template_name = "booksite/login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Account logged in successfully")
        return super(),form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials!")
        return super().form_invalid(form)

class LogoutClassView(LogoutView):
    next_page = reverse_lazy('login')
    
    def post(self, request, *args, **kwargs):
        messages.success(self.request, "Account logged out successfully!")
        return super().post(self.request, *args, **kwargs)
