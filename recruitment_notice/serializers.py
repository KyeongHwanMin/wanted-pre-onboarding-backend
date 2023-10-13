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


class RecruitmentNoticeListSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.CharField(source="id")
    회사명 = serializers.CharField(source="company.name", read_only=True)
    국가 = serializers.CharField(source="company.nation", read_only=True)
    지역 = serializers.CharField(source="company.area", read_only=True)
    채용포지션 = serializers.CharField(source="position")
    채용보상금 = serializers.IntegerField(source="compensation")
    사용기술 = serializers.CharField(source="skill")

    class Meta:
        model = RecruitmentNotice
        fields = [
            "채용공고_id",
            "회사명",
            "국가",
            "지역",
            "채용포지션",
            "채용보상금",
            "사용기술",
        ]


class RecruitmentNoticeDetailSerializer(serializers.ModelSerializer):
    채용공고_id = serializers.CharField(source="id")
    회사명 = serializers.CharField(source="company.name", read_only=True)
    국가 = serializers.CharField(source="company.nation", read_only=True)
    지역 = serializers.CharField(source="company.area", read_only=True)
    채용포지션 = serializers.CharField(source="position")
    채용보상금 = serializers.IntegerField(source="compensation")
    사용기술 = serializers.CharField(source="skill")
    채용내용 = serializers.CharField(source="content")
    회사가올린다른채용공고 = serializers.SerializerMethodField()

    class Meta:
        model = RecruitmentNotice
        fields = [
            "채용공고_id",
            "회사명",
            "국가",
            "지역",
            "채용포지션",
            "채용보상금",  # POST를 위해 필요
            "사용기술",
            "채용내용",
            "회사가올린다른채용공고",
        ]

    # get_<field_name>의 형식
    def get_회사가올린다른채용공고(self, obj):
        other_recruitment_notices = RecruitmentNotice.objects.filter(
            company=obj.company
        ).exclude(id=obj.id)
        return [notice.id for notice in other_recruitment_notices]
