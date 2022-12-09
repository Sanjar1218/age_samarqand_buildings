from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from home.models import Building
from home.serializers import BuildingSerializer

import json


def home(requests: HttpRequest) -> HttpResponse:
    all_buldings = Building.objects.all()
    lst = []
    serializer = BuildingSerializer(all_buldings, many=True)
    for i in serializer.data:
        lst.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": i["coordinates"]
            }
        })
    return render(requests,
                  'pages/home_page.html',
                  context={'data': json.dumps(lst)})


def osmbuilding(requests: HttpRequest) -> HttpResponse:
    return render(requests, "home.html")


def leaflet(requests: HttpRequest) -> HttpResponse:
    return render(requests, "leaflet.html")


def django_leaflet(requests: HttpRequest) -> HttpResponse:
    all_buldings = Building.objects.all()
    lst = []
    serializer = BuildingSerializer(all_buldings, many=True)
    for i in serializer.data:
        lst.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": i["coordinates"]
            }
        })

    return render(requests,
                  "django_leaflet.html",
                  context={"data": json.dumps(lst)})
