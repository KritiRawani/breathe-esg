from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import (
    approve_record,
    reject_record,
    lock_record
)


class ApproveRecordAPIView(APIView):

    def post(self, request, record_id):

        reviewed_by = request.data.get('reviewed_by')

        record = approve_record(
            record_id,
            reviewed_by
        )

        return Response(
            {
                "message": f"Record {record.id} approved"
            },
            status=status.HTTP_200_OK
        )


class RejectRecordAPIView(APIView):

    def post(self, request, record_id):

        reviewed_by = request.data.get('reviewed_by')

        record = reject_record(
            record_id,
            reviewed_by
        )

        return Response(
            {
                "message": f"Record {record.id} rejected"
            },
            status=status.HTTP_200_OK
        )


class LockRecordAPIView(APIView):

    def post(self, request, record_id):

        reviewed_by = request.data.get('reviewed_by')

        record = lock_record(
            record_id,
            reviewed_by
        )

        return Response(
            {
                "message": f"Record {record.id} locked"
            },
            status=status.HTTP_200_OK
        )