from django.views.generic import ListView

from flightmanager.models import Flight


# flight list
class FlightListView(ListView):
    model = Flight
    template_name = 'flights/flights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        return context

# each flight page


# each flight page reserve
