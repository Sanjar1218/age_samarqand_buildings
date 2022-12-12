from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:id>', views.update_home),
    path('osm', views.osmbuilding),
    path('leaflet', views.leaflet),
    path('django_leaflet', views.django_leaflet)
]
