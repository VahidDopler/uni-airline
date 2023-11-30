from django.shortcuts import render, redirect

from buyingmanager.forms import TicketForm
from .models import Ticket


def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_all_ticket')
    else:
        form = TicketForm()

    context = {'form': form}
    return render(request, 'tickets/create.html', context)


def list_tickets(request):
    tickets = Ticket.objects.all()
    context = {'tickets': tickets}
    return render(request, 'tickets/ticket_list.html', context)
