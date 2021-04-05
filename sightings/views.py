from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def view_map(request):
    sights = []
    context = {
        'sights': sights,
    }
    return render(request, 'sightings/map.html', context)
