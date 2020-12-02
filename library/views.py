from django.shortcuts import render
from django.http import HttpResponse
from .models import Cryptid, Location, Sighting
from datetime import date

def index(request):
    return HttpResponse('Hello!')

def cryptids(request):
    context = {'cryptids': Cryptid.objects.all()}
    return render(request, 'library/cryptids.html', context)

def cryptid_detail(request, cryptid_id):
    context = {'cryptid': Cryptid.objects.get(pk=cryptid_id)
        }
    return render(request, 'library/cryptid_detail.html', context)

def cryptid_sightings(request, cryptid_id):
    return HttpResponse('Cryptid sightings')

def locations(request):
    context = {'locations': Location.objects.all()}
    return render(request, 'library/map.html', context)

def location_detail(request, location_id):
    return HttpResponse('location details')

def sightings_continent(request, continent):
    context = {
        'sightings': Sighting.objects.filter(location__continent__icontains = continent),
        'location': Location.objects.all(),
        'cryptid': Cryptid.objects.all()}
    return render(request, 'library/continent.html', context)

def location_sightings(request, location_id):
    return HttpResponse('location sightings')

def sightings_year(request, year):
    context = {'sightings': Sighting.objects.filter(date__year = year), 'date': date(year, 1, 1), 'type': 'year'}
    return render(request, 'library/sightings.html', context)
    
def sightings_year_month(request, year, month):
    context = {'sightings': Sighting.objects.filter(date__year = year).filter(date__month = month), 'date': date(year, month, 1), 'type': 'month'}
    return render(request, 'library/sightings.html', context)

def sightings_year_month_day(request, year, month, day):
    context = {'sightings': Sighting.objects.filter(date__year = year).filter(date__month = month).filter(date__day = day),'date': date(year, month, day), 'type': 'day'}
    return render(request, 'library/sightings.html', context)





