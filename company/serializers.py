from rest_framework.serializers import ModelSerializer
from .models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "nation", "area"]


class CreateCompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "nation", "area"]
