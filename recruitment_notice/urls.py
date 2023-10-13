from django.urls import path
from recruitment_notice.views import RecruitmentNoticeView

urlpatterns = [
    path("", RecruitmentNoticeView.as_view()),
]
