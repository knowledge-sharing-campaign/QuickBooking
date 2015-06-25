import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

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
    bus_routes_date1 = request.POST['FirstDate']
    bus_routes_date2 = request.POST['SecondDate']
    routes = []

    for route in BusRoute.objects.all():
        date =  DateFormat(route.timing.date).format("m/d/Y")

        if date == bus_routes_date1:
            routes.append(route)

    template = loader.get_template('QuickBooking/results.html')
    context = RequestContext(request, {
        'bus_routes': routes,
        'bus_routes_date1': bus_routes_date1,
        'bus_routes_date2': bus_routes_date2
    })
  
    return HttpResponse(template.render(context))
