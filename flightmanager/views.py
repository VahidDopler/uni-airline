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
    all_air = Airport.objects.all()
    if request.method == 'GET':
        errors = {'origin': 'Please select an origin airport.',
                  'destination': 'Please select a destination airport.'}
        context = {'errors': errors, 'origin_airports': all_air, 'destination_airports': all_air}
        return render(request, 'flights/search.html', context)
    if request.method == "POST":
        origin_id = request.POST.get('origin')
        destination_id = request.POST.get('destination')
        if origin_id and destination_id:
            origin_id = int(origin_id)
            destination_id = int(destination_id)
            flights = Flight.objects.filter(origin_id=origin_id, destination_id=destination_id)
            context = {"flights": flights, 'origin_airports': all_air, 'destination_airports': all_air}
            return render(request, 'flights/search.html', context)
        else:
            context = {'origin_airports': all_air, 'destination_airports': all_air}
            return render(request, 'flights/search.html', context)
# each flight page


# each flight page reserve
