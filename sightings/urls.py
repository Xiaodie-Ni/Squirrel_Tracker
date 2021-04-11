"""squirrel_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sightings import views

urlpatterns = [
    path("map/", views.view_map, name='map'),
    path("sightings/", views.list_sightings, name='sightings'),
    path('sightings/add/', views.add_sighting, name='add'),
    path('sightings/stats/', views.get_general_stats, name='stats'),
    path('sightings/<unique_id>/', views.update_sighting, name='update'),
]
