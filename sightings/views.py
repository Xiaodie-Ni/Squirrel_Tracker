from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse
from .models import Sighting
from .forms import SightingForm


def view_map(request):
    sightings = Sighting.objects.all()[:100]
    fields = ["longitude", "latitude"]
    context = {
        "sightings": sightings,
        "fields": fields,
    }
    return render(request, "sightings/map.html", context)


def list_sightings(request):
    sightings = Sighting.objects.all()
    fields = ["longitude", "latitude", "unique_squirrel_id", "shift", "date", "age"]
    context = {
        "sightings": sightings,
        "fields": fields,
    }
    return render(request, "sightings/sightings.html", context)


def update_sighting(request, unique_id):
    obj = get_object_or_404(Sighting, unique_squirrel_id=unique_id)
    if request.method == "POST":
        form = SightingForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect("/sightings/")
    else:
        form = SightingForm(instance=obj)
        context = {
            "form": form,
        }
        return render(request, "sightings/update.html", context)


def add_sighting(request):
    if request.method == "POST":
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/sightings/")
    else:
        form = SightingForm()
        context = {'form': form, }
        return render(request, "sightings/add.html", context)


def get_general_stats(request):
    num_sightings = Sighting.objects.all().count()
    num_adults = Sighting.objects.filter(age="Adult").count()
    num_gray = Sighting.objects.filter(primary_fur_color="Gray").count()
    num_running = Sighting.objects.filter(running=True).count()
    num_eating = Sighting.objects.filter(eating=True).count()
    context = {
        "num_sightings": num_sightings,
        "num_adults": num_adults,
        "num_gray": num_gray,
        "num_running": num_running,
        "num_eating": num_eating,
    }
    return render(request, "sightings/stats.html", context)
