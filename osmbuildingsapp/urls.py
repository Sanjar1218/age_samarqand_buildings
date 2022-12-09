from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('osm', views.osmbuilding),
    path('leaflet', views.leaflet),
    path('django_leaflet', views.django_leaflet)
]
