from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pupils/', include('app_pupils.urls')),
    path('', include('app_pages.urls')),
]
