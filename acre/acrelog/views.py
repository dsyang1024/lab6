from django.shortcuts import render
from .models import event, location, log, operation, operator, seed, fertilizer, spray
# Create your views here.
from django.http import HttpResponse
from django.http import Http404

import geojson
import shapely.geometry as geo


def index(request):
    latest_fields = location.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'index.html', context)



def fields(request, location_id):
    logs = log.objects.filter(location=location_id)
    print (logs)
    field = location.objects.get(pk=location_id)
    
    context = {'field':field, 'logs': logs}

    return render(request, 'fields.html', context)



def render_map(request):
    point = geo.Point(([-86.99269856365936, 40.470060621973026]))
    marker = geojson.Feature(geometry=point, properties={"message": "Hello World"})
    data = geojson.FeatureCollection(marker)
    return render(request, "map.html", {"data": data})