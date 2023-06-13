# views.py

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place

def show_main_page(request):


    geo_json_dict = {'type': 'Feature Collection', 'features': []}

    places_set = Place.objects.all()

    for place in places_set.iterator():
        geometry_dict = dict.fromkeys({'type', 'coordinates'})
        properties_dict = dict.fromkeys({'title', 'placeId', 'detailsUrl'})
        geo_json_features_dict = dict.fromkeys({'type', 'geometry', 'properties'})

        title = place.title
        coordinates = [place.latitude, place.longtitude]

        geometry_dict['type'] = 'Point'
        geometry_dict['coordinates'] = coordinates

        properties_dict['title'] = place.title
        properties_dict['placeId'] = place.title
        properties_dict['detailsUrl'] = 'XXX'

        geo_json_features_dict['type'] = 'Feature'
        geo_json_features_dict['geometry'] = geometry_dict
        geo_json_features_dict['properties'] = properties_dict

        geo_json_dict['features'].append(geo_json_features_dict)

    return render(request, 'index.html')