import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Bus, BusStop, BusRoute

def index(request):
    bus_stop_list = BusStop.objects.all()
    bus_stop_names = [stop.stopname for stop in bus_stop_list]
    template = loader.get_template('QuickBooking/index.html')
    context = RequestContext(request, {
        'bus_stop_list': bus_stop_list,
        'bus_stop_names': json.dumps(bus_stop_names)
    })

    return HttpResponse(template.render(context))

def results(request):
    bus_routes = BusRoute.objects.filter(src=request.POST['src'], dest=request.POST['dest'])
    template = loader.get_template('QuickBooking/results.html')
    context = RequestContext(request, {
        'bus_routes': bus_routes

    })
  
    return HttpResponse(template.render(context))
