from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from recruitment_notice.models import RecruitmentNotice
from recruitment_notice.serializers import (
    RecruitmentNoticeWriteSerializer,
    RecruitmentNoticeUpdateSerializer,
)


class RecruitmentNoticeView(APIView):
    def post(self, request):
        serializer = RecruitmentNoticeWriteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecruitmentNoticeDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(RecruitmentNotice, pk=pk)

    def patch(self, request, pk):
        recruitment_notice_info = self.get_object(pk)

        serializer = RecruitmentNoticeUpdateSerializer(
            recruitment_notice_info, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
