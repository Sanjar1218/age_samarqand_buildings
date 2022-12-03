from django.urls import path
from . import views


urlpatterns = [
    path('osm', views.home),
    path('leaflet', views.home),
]
