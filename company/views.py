from rest_framework import status
from rest_framework.response import Response
from company.models import Company
from rest_framework.views import APIView
from company.serializers import CreateCompanySerializer, CompanySerializer


class CompanyView(APIView):
    def get(self, request):
        qs = Company.objects.all()
        serializer = CompanySerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
