from django.db import models
from tenants.models import Tenant
from ingestion.models import RawRecord


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'PENDING'),
        ('FLAGGED', 'FLAGGED'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
        ('LOCKED', 'LOCKED'),
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    source_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    scope = models.CharField(max_length=20)

    category = models.CharField(max_length=100)

    activity_value = models.FloatField()

    original_unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    normalized_value = models.FloatField()

    emission_kg_co2e = models.FloatField()

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    is_suspicious = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.emission_kg_co2e} kgCO2e"