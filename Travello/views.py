from django.shortcuts import render

from Travello.models import Destination


# Create your views here.


def index(request):
    dest1 = Destination()
    dest1.LocationName = 'Delhi'
    return render(request, 'index.html', {'dest1': dest1})
