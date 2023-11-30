from django import forms
from buyingmanager.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['user', 'flight', 'seat_number', 'price']

    def clean_seat_number(self):
        seat_number = self.cleaned_data['seat_number']
        # Check if the seat number is already taken for the same flight
        existing_tickets = Ticket.objects.filter(flight=self.cleaned_data['flight'])
        for ticket in existing_tickets:
            if ticket.seat_number == seat_number:
                raise forms.ValidationError('Seat number is already taken for this flight.')
        return seat_number
