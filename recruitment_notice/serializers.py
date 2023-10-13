from rest_framework import serializers
from recruitment_notice.models import RecruitmentNotice


class RecruitmentNoticeWriteSerializer(serializers.ModelSerializer):
    회사_id = serializers.IntegerField(source="company_id")
    채용포지션 = serializers.CharField(source="position")
    채용보상금 = serializers.IntegerField(source="compensation")
    채용내용 = serializers.CharField(source="content")
    사용기술 = serializers.CharField(source="skill")

    class Meta:
        model = RecruitmentNotice
        fields = [
            "회사_id",
            "채용포지션",
            "채용보상금",
            "채용내용",
            "사용기술",
        ]


class RecruitmentNoticeUpdateSerializer(serializers.ModelSerializer):
    채용포지션 = serializers.CharField(source="position")
    채용보상금 = serializers.IntegerField(source="compensation")
    채용내용 = serializers.CharField(source="content")
    사용기술 = serializers.CharField(source="skill")

    class Meta:
        model = RecruitmentNotice
        fields = [
            "채용포지션",
            "채용보상금",
            "채용내용",
            "사용기술",
        ]
