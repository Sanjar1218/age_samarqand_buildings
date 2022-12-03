from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('osmbuildingsapp.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
]
