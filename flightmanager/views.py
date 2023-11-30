from django.shortcuts import render
from django.views.generic import ListView

from flightmanager.models import Flight, Airport


# flight list
class FlightListView(ListView):
    model = Flight
    template_name = 'flights/flights.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flights'] = Flight.objects.all()
        return context


# search flight page
def search_flights(request):
    if request.method == 'GET':
        all_air = Airport.objects.all()
        errors = {'origin': 'Please select an origin airport.',
                  'destination': 'Please select a destination airport.'}
        context = {'errors': errors, 'origin_airports': all_air, 'destination_airports': all_air}
        return render(request, 'flights/search.html', context)
    if request.method == "POST":
        print(request.POST.get("origin"))
        print(request.POST.get("destination"))
        all_air = Airport.objects.all()
        errors = {'origin': 'Please select an origin airport.',
                  'destination': 'Please select a destination airport.'}
        context = {'errors': errors, 'origin_airports': all_air, 'destination_airports': all_air}
        return render(request, 'flights/search.html', context)
# each flight page


# each flight page reserve
