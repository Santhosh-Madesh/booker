from django.urls import path
from . import views
from .views import BookingCreate, UserDashboard, UserDashboardCreate, UserDashboardDelete, UserDashboardUpdate
from .auth import SignUpView, LoginClassView, LogoutClassView

urlpatterns=[
    path("", views.home, name="home"),
    path("create/", BookingCreate.as_view(), name="create"),
    path("auth/signup/", SignUpView.as_view(), name="signup"),
    path("auth/login/", LoginClassView.as_view(), name="login"),
    path("auth/logout/", LogoutClassView.as_view(), name="logout"),
    path("dashboard/", UserDashboard.as_view(), name="dashboard"),
    path("dashboard/create/", UserDashboardCreate.as_view(), name="dashboard_create"),
    path("dashboard/delete/<int:pk>", UserDashboardDelete.as_view(), name="dashboard_delete"),
    path("dashboard/update/<int:pk>", UserDashboardUpdate.as_view(), name="dashboard_update"),
]