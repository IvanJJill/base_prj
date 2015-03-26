from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bikes index.")


def bike_details(request, bike_id):
    response = "Read bike's %s details"
    return HttpResponse(response % bike_id)


def order_details(request, order_id):
    response = "Read order's %s details"
    return HttpResponse(response % order_id)