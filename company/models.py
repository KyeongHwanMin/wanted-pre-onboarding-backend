from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, help_text="회사명")
    nation = models.CharField(max_length=128, help_text="국가")
    area = models.CharField(max_length=255, help_text="지역")
    created_at = models.DateTimeField(auto_now_add=True, help_text="생성 날짜")
    modified_at = models.DateTimeField(auto_now=True, help_text="수정 날짜")

    class Meta:
        db_table = "company"
