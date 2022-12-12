from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from home.models import Building
from home.serializers import BuildingSerializer

import json


def update_home(request: HttpRequest, id) -> HttpResponse:
    setviews = request.POST.get('setviews', [39.6487765, 66.9618944])
    setviews = list(
        map(float,
            setviews.split('(')[-1].split(')')[0].split(',')))
    request.session['setview'] = [setviews[0], setviews[1]]
    if request.method == 'POST':
        building = Building.objects.get(id=id)
        serializer = BuildingSerializer(building,
                                        data=request.POST,
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return redirect('home')
        return redirect('home')


def home(requests: HttpRequest) -> HttpResponse:
    setviews = requests.session.get('setview', [39.6487765, 66.9618944])
    print('home', setviews)
    all_buldings = Building.objects.all()
    lst = []
    serializer = BuildingSerializer(all_buldings, many=True)
    for i in serializer.data:
        lst.append({
            "type": "Feature",
            "id": i['id'],
            "address": i['address'],
            "type_of_building": i['type_of_building'],
            "age": i['date'],
            "geometry": {
                "type": "Polygon",
                "coordinates": i["coordinates"]
            }
        })
    return render(requests,
                  'pages/home_page.html',
                  context={
                      'data': json.dumps(lst),
                      'setviews': json.dumps(setviews)
                  })


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
