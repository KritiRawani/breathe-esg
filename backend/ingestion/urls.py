from django.urls import path

from .views import SAPUploadAPIView


urlpatterns = [
    path(
        'upload/sap/',
        SAPUploadAPIView.as_view(),
        name='upload-sap'
    ),
]