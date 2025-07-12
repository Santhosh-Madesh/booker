from django.urls import path
from . import views
from .views import BookingCreate
from .auth import SignUpView, LoginClassView

urlpatterns=[
    path("", views.home, name="home"),
    path("create/", BookingCreate.as_view(), name="create"),
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/login/", LoginClassView.as_view(), name="login"),
]