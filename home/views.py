from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .serializers import BuildingSerializer
from .models import Building


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

    serializer = BuildingSerializer(all_buldings, many=True)

    return Response({'buldings': serializer.data})


@api_view(['POST'])
def update_home(request: Request, id) -> Response:
    building = Building.objects.get(id=id)
    serializer = BuildingSerializer(building, data=request.data)
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
