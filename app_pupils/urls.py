from django.urls import path

from .views import pupils_list, pupils_detail

urlpatterns = [
    path('', pupils_list, name='pupils_list'),
    path('<int:pk>/', pupils_detail, name='pupil_info'),
]