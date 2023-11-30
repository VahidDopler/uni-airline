from django.urls import path
from .views import create_ticket, list_tickets
from django.urls import path

from .views import create_ticket, list_tickets

urlpatterns = [
    path('create/', create_ticket, name="creating_ticket"),
    path('all/', list_tickets, name="list_of_all_ticket")
]
