from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
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
    success_url = reverse_lazy('home')