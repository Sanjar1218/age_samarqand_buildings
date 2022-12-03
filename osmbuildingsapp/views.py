from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from home.models import Building
from home.serializers import BuildingSerializer


def osmbuilding(requests: HttpRequest) -> HttpResponse:
    return render(requests, 'home.html')


def leaflet(requests: HttpRequest) -> HttpResponse:
    return render(requests, 'leaflet.html')


def django_leaflet(requests: HttpRequest) -> HttpResponse:
    all_buldings = Building.objects.all()

    serializer = BuildingSerializer(all_buldings, many=True)

    print(serializer.data)
    return render(requests, 'django_leaflet.html', context={'data': serializer.data})
