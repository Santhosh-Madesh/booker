from django.urls import path, register_converter
from .converters import DateConverter
from . import views
from .views import BookingCreate, UserDashboard, UserDashboardCreate, UserDashboardDelete, UserDashboardUpdate
from .auth import SignUpView, LoginClassView, LogoutClassView

register_converter(DateConverter, 'date')

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
    path("contact/", views.contact, name="contact"),
    path("selectDate/", views.selectDate, name="selectDate"),
    path("date/<date:book_date>", views.selectSlot, name="date" ),
    path("book/<date:book_date>/<int:book_slot>/", views.booking, name="book"),
]