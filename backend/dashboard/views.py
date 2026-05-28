from rest_framework.views import APIView
from rest_framework.response import Response

from emissions.models import EmissionRecord


class DashboardSummaryAPIView(APIView):

    def get(self, request):

        total_records = EmissionRecord.objects.count()

        approved_records = EmissionRecord.objects.filter(
            status='APPROVED'
        ).count()

        rejected_records = EmissionRecord.objects.filter(
            status='REJECTED'
        ).count()

        flagged_records = EmissionRecord.objects.filter(
            is_suspicious=True
        ).count()

        pending_records = EmissionRecord.objects.filter(
            status='PENDING'
        ).count()

        total_emissions = sum(
            EmissionRecord.objects.values_list(
                'emission_kg_co2e',
                flat=True
            )
        )

        return Response({
            "total_records": total_records,
            "approved_records": approved_records,
            "rejected_records": rejected_records,
            "flagged_records": flagged_records,
            "pending_records": pending_records,
            "total_emissions_kg_co2e": total_emissions
        })