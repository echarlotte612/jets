from django.shortcuts import render
from django.http import HttpResponse
from .models import Cryptid, Location, Sighting

def index(request):
    return HttpResponse('Hello!')

def cryptids(request):
    context = {'cryptids': Cryptid.objects.all()}
    return render(request, 'library/cryptids.html', context)
  

def cryptid_detail(request, cryptid_id):
    context = {'cryptid': Cryptid.objects.get(pk=cryptid_id), 
        'locations': Location.objects.filter(cryptid__pk=cryptid_id),
        'sightings': Sighting.objects.filter(cryptid__pk=cryptid_id)
        }
    return render(request, 'library/cryptid_detail.html', context)

def cryptid_sightings(request, cryptid_id):
    return HttpResponse('Cryptid sightings')

def locations(request):
    return HttpResponse('locations')

def location_detail(request, location_id):
    return HttpResponse('location details')

def location_sightings(request, location_id):
    return HttpResponse('location sightings')



