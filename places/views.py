# views.py

import json
import pprint

from collections import OrderedDict
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place, Image


def show_main_page(request):

    geo_json_dict = {'type': 'Feature Collection', 'features': []}

    places_set = Place.objects.all()

    for place in places_set.iterator():

        feature_dict = OrderedDict()
        geometry_dict = OrderedDict()
        properties_dict = OrderedDict()

        title = place.title
        coordinates = [place.longtitude, place.latitude]

        geometry_dict['type'] = 'Point'
        geometry_dict['coordinates'] = coordinates

        properties_dict['title'] = title
        properties_dict['placeId'] = place.id
        properties_dict['detailsUrl'] = reverse('place_info', args=[place.id])

        feature_dict['type'] = 'Feature'
        feature_dict['geometry'] = geometry_dict
        feature_dict['properties'] = properties_dict

        geo_json_dict['features'].append(dict(feature_dict))

    return render(request, 'index.html', {'value': geo_json_dict})

def get_location_title_by_id(request, id):

    place = get_object_or_404(Place, id=id)

    coordinates = OrderedDict()
    images = []

    title = place.title
    description_short = place.description_short
    description_long = place.description_long
    latitude = place.latitude
    longtitude = place.longtitude

    coordinates['lat'] = latitude
    coordinates['lng'] = longtitude


    images_set = place.images.all()
    for image in images_set:
        images.append(image.image.url)

    place_description = {
        'title': title,
        'imgs': images,
        'description_short': description_short,
        'description_long': description_long,
        'coordinates': coordinates
    }

    return JsonResponse(dict(place_description), safe=False)
