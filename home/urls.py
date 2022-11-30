from django.urls import path
from . import views

urlpatterns = [
    # CRUD
    path('create_home', views.create_home),
    path('get_homes', views.get_homes),
    path('update_home/<int:id>', views.update_home),
    path('delete_home/<int:id>', views.delete_home),
]
