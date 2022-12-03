from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def osmbuilding(requests: HttpRequest) -> HttpResponse:
    return render(requests, 'home.html')


def leaflet(requests: HttpRequest) -> HttpResponse:
    return render(requests, 'leaflet.html')
