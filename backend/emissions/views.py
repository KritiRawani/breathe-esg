from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework import serializers

from .services import calculate_emissions

from .models import EmissionRecord


class NormalizeEmissionAPIView(APIView):

    def post(self, request):

        calculate_emissions()

        return Response(
            {
                "message": "Emission normalization completed"
            },
            status=status.HTTP_200_OK
        )
    
class EmissionRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmissionRecord
        fields = '__all__'


class EmissionRecordListAPIView(ListAPIView):

    queryset = EmissionRecord.objects.all().order_by('-id')

    serializer_class = EmissionRecordSerializer