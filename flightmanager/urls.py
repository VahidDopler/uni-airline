from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path("all/", views.FlightListView.as_view(), name="all_flights"),
]
