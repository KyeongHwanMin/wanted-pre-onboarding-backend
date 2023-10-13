from rest_framework import serializers
from recruitment_support.models import Support


class RecruitmentSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Support
        fields = ["recruitment_notice", "user"]
