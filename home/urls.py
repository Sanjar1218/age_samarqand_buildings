from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # CRUD
    path('create_home', views.create_home),
    path('get_home', views.get_home),
    path('update_home', views.update_home),
    path('delete_home', views.delete_home),
]
