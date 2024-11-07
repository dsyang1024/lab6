from django.shortcuts import render
from .models import event, location, log, operation, operator, seed, fertilizer, spray
# Create your views here.
from django.http import HttpResponse
from django.http import Http404



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
