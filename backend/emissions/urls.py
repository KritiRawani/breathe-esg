from django.urls import path

from .views import (
    NormalizeEmissionAPIView,
    EmissionRecordListAPIView
)


urlpatterns = [

    path(
        'normalize/',
        NormalizeEmissionAPIView.as_view(),
        name='normalize-emissions'
    ),

    path(
        'records/',
        EmissionRecordListAPIView.as_view(),
        name='emission-records'
    ),
]