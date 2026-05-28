from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'api/',
        include('ingestion.urls')
    ),

    path(
        'api/emissions/',
        include('emissions.urls')
    ),

    path(
        'api/reviews/',
        include('reviews.urls')
    ),

    path(
        'api/dashboard/',
        include('dashboard.urls')
    ),
]