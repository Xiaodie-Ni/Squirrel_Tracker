from django.shortcuts import render

from django.http import HttpResponse
from .models import Sighting


def index(request):
    return HttpResponse("Hello, world. ")


def view_map(request):
    sights = Sighting.objects.all()[:100]
    context = {
        'sights': sights,
    }
    return render(request, 'sightings/map.html', context)
