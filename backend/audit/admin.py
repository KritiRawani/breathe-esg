from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'emission_record',
        'action',
        'changed_by',
        'timestamp'
    )

    list_filter = (
        'action',
    )