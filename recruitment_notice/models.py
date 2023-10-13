from django.db import models


class RecruitmentNotice(models.Model):
    company = models.ForeignKey(
        to="company.Company",
        on_delete=models.CASCADE,
        related_name="recruitment_notices",
        help_text="회사 ID",
    )
    position = models.CharField(max_length=50, help_text="채용 포지션")
    compensation = models.SmallIntegerField(default=0, help_text="채용 보상금")
    content = models.TextField(blank=True)
    skill = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 날짜")
    modified_at = models.DateTimeField(auto_now=True, help_text="수정 날짜")

    class Meta:
        db_table = "recruitmentNotice"
