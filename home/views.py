from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .serializers import BuildingSerializer
from .models import Building

import json


@api_view(['POST'])
def create_home(request: Request) -> Response:
    serializer = BuildingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'created'})

    return Response({'status': 'bad', 'errros': serializer.errors})


@api_view(['GET'])
def get_homes(request: Request) -> Response:
    all_buldings = Building.objects.all()
    lst = []
    setviews = [39.6487765, 66.9618944]

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

    return Response({'buildings': lst, 'setviews': setviews})


@api_view(['POST'])
def update_home(request: Request, id) -> Response:
    building = Building.objects.get(id=id)
    serializer = BuildingSerializer(building, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'updated'})
    return Response({'status': serializer.errors})


@api_view(['POST'])
def delete_home(request: Request, id) -> Response:
    try:
        building = Building.objects.get(id=id)
        building.delete()
        return Response({'status': 'deleted'})

    except ObjectDoesNotExist:
        return Response({'status': 'does not exists bulding'})

    except MultipleObjectsReturned:
        return Response({'status': 'multiple objects returned'})
