from django.contrib import admin
from .models import DataSource, RawRecord


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'tenant',
        'source_type',
        'uploaded_file_name',
        'uploaded_by',
        'uploaded_at'
    )

    list_filter = (
        'source_type',
    )


@admin.register(RawRecord)
class RawRecordAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'data_source',
        'processing_status',
        'created_at'
    )

    list_filter = (
        'processing_status',
    )