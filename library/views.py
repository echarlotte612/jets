from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello!')

def cryptids(request):
    return HttpResponse('Cryptids')

def cryptid_detail(request, cryptid_id):
    return HttpResponse('Cryptid detail')

def cryptid_sightings(request, cryptid_id):
    return HttpResponse('Cryptid sightings')

def locations(request):
    return HttpResponse('locations')

def location_detail(request, location_id):
    return HttpResponse('location details')

def location_sightings(request, location_id):
    return HttpResponse('location sightings')


# Create your views here.
