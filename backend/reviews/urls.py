from django.urls import path

from .views import (
    ApproveRecordAPIView,
    RejectRecordAPIView,
    LockRecordAPIView
)


urlpatterns = [

    path(
        'approve/<int:record_id>/',
        ApproveRecordAPIView.as_view(),
        name='approve-record'
    ),

    path(
        'reject/<int:record_id>/',
        RejectRecordAPIView.as_view(),
        name='reject-record'
    ),

    path(
        'lock/<int:record_id>/',
        LockRecordAPIView.as_view(),
        name='lock-record'
    ),
]