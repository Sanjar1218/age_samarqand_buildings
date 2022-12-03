from django.urls import path
from . import views


urlpatterns = [
    path('osm', views.osmbuilding),
    path('leaflet', views.leaflet),
]
