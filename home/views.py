from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view

from .serializers import BuildingSerializer


@api_view(['POST'])
def create_home(request: Request) -> Response:
    serializer = BuildingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'created'})
    return Response({'status': 'bad', 'errros': serializer.errors})


@api_view(['GET'])
def get_home(request: Request) -> Response:
    pass
