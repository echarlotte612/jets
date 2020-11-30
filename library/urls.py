from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cryptids/', views.cryptids, name = 'cryptids'),
    path('cryptids/<int:cryptid_id>/', views.cryptid_detail, name = 'cryptid_detail'),
    path('cryptids/<int:cryptid_id>/sightings/', views.cryptid_sightings, name = 'cryptid_sightings'),
    path('locations/', views.locations, name = 'locations'),
    path('locations/<int:location_id>/', views.location_detail, name = 'location_detail'),
    path('locations/<int:location_id>/sightings/', views.location_sightings, name = 'location_sightings'),
]