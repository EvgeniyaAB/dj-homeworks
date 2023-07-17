from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv

def index(request):
    return redirect(reverse('bus_stations'))

with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stations_list = []
    for row in reader:
        bus_stations_list.append(
            {'Name': row['Name'],
             'Street': row['Street'],
             'District': row['District']
             }
        )

def bus_stations(request):

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 20)
    page_obj = paginator.get_page(page_number)

    context = {
        'bus_stations': page_obj.object_list,
        'page': page_obj,
    }
    return render(request, 'stations/index.html', context)
