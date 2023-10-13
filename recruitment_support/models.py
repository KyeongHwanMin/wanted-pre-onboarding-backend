from django.db import models


class Support(models.Model):
    user = models.OneToOneField(to="account.User", on_delete=models.CASCADE)
    recruitment_notice = models.ForeignKey(
        to="recruitment_notice.RecruitmentNotice", on_delete=models.SET_NULL, null=True
    )

    class Meta:
        db_table = "support"
