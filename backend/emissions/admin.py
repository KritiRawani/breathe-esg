from django.contrib import admin
from .models import EmissionRecord


@admin.register(EmissionRecord)
class EmissionRecordAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'tenant',
        'scope',
        'category',
        'emission_kg_co2e',
        'status',
        'is_suspicious'
    )

    list_filter = (
        'scope',
        'status',
        'is_suspicious'
    )

    search_fields = (
        'category',
    )