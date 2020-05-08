from django.shortcuts import render

from Travello.models import Destination


# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.LocationName = 'Delhi'
    dest1.Description = 'The city that never sleep'
    dest1.Image = 'destination_1.jpg'
    dest1.Price = 700
    dest1.Offer = False

    dest2 = Destination()
    dest2.LocationName = 'Mumbai'
    dest2.Description = 'The Famous Vada Pao City'
    dest2.Image = 'destination_2.jpg'
    dest2.Price = 650
    dest2.Offer = True

    dest3 = Destination()
    dest3.LocationName = 'Bengaluru'
    dest3.Description = 'IT Hub'
    dest3.Image = 'destination_3.jpg'
    dest3.Price = 750
    dest3.Offer = True

    dests = [dest1, dest2, dest3]
    return render(request, 'index.html', {'dests': dests})
