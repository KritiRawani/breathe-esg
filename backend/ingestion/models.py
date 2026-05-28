from django.db import models
from tenants.models import Tenant


class DataSource(models.Model):

    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'UTILITY'),
        ('TRAVEL', 'TRAVEL'),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=50,
        choices=SOURCE_TYPES
    )

    uploaded_file_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    uploaded_by = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tenant.name} - {self.source_type}"
    
class RawRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('PROCESSED', 'PROCESSED'),
        ('FAILED', 'FAILED'),
    ]

    data_source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    raw_data = models.JSONField()

    processing_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    error_message = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Raw Record {self.id}"