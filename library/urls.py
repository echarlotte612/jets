from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cryptids/', views.cryptids, name = 'cryptids'),
    path('cryptids/<int:cryptid_id>/', views.cryptid_detail, name = 'cryptid_detail'),
    path('cryptids/<int:cryptid_id>/sightings/', views.cryptid_sightings, name = 'cryptid_sightings'),
    path('cryptids/tags/<str:tag>/', views.cryptid_tags, name = 'cryptid_tags'),
    path('locations/', views.locations, name = 'locations'),
    path('locations/<int:location_id>/', views.location_detail, name = 'location_detail'),
    path('locations/<int:location_id>/sightings/', views.location_sightings, name = 'location_sightings'),
    path('sightings/<int:year>/', views.sightings_year, name = 'sightings_year'),
    path('sightings/<int:year>/<int:month>/', views.sightings_year_month, name = 'sightings_year_month'),
    path('sightings/<int:year>/<int:month>/<int:day>/', views.sightings_year_month_day, name = 'sightings_year_month_day')
]