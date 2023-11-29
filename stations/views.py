import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    path = BUS_STATION_CSV
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        info = []
        for row in reader:
            info.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    # print('AAAAAAAAAA', info)
    paginator = Paginator(info, 10)
    page_number = int(request.GET.get("page", 1))
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    print('PAGE', page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    print('CONTEXT', context)
    return render(request, 'stations/index.html', context)
