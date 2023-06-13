# views.py

import json
import pprint

from collections import OrderedDict
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from places.models import Place

def show_main_page(request):


    geo_json_dict = {'type': 'Feature Collection', 'features': []}

    places_set = Place.objects.all()

    for place in places_set.iterator():

        feature_dict =  OrderedDict()
        geometry_dict = OrderedDict()
        properties_dict = OrderedDict()


        title = place.title
        coordinates = [place.longtitude, place.latitude]

        geometry_dict['type'] = 'Point'
        geometry_dict['coordinates'] = coordinates

        properties_dict['title'] = title
        properties_dict['placeId'] = title
        properties_dict['detailsUrl'] = 'XXX'

        feature_dict['type'] = 'Feature'
        feature_dict['geometry'] = geometry_dict
        feature_dict['properties'] =properties_dict

        geo_json_dict['features'].append(dict(feature_dict))


    return render(request, 'index.html', {'value':geo_json_dict})