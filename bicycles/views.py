from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from bicycles.models import Bicycle, Order, Client


def index(request):
    bicycles_list = Bicycle.objects.order_by('-type_make')[:5]
    template = loader.get_template('bicycles/index.html')
    context = RequestContext(request, {
        'bicycles_list':bicycles_list,

    })
    return HttpResponse(template.render(context))


def bike_details(request, bike_id):
    response = "Read bike's %s details"
    return HttpResponse(response % bike_id)


def order_details(request, order_id):
    response = "Read order's %s details"
    return HttpResponse(response % order_id)