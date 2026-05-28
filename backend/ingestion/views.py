from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileUploadSerializer
from .services import process_sap_csv


class SAPUploadAPIView(APIView):

    def post(self, request):

        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():

            file = serializer.validated_data['file']

            uploaded_by = serializer.validated_data['uploaded_by']

            data_source = process_sap_csv(
                file,
                uploaded_by
            )

            return Response(
                {
                    "message": "SAP CSV uploaded successfully",
                    "data_source_id": data_source.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )