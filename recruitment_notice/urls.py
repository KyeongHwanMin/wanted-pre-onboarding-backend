from django.urls import path
from recruitment_notice.views import RecruitmentNoticeView, RecruitmentNoticeDetailView

urlpatterns = [
    path("", RecruitmentNoticeView.as_view()),
    path("/<int:pk>", RecruitmentNoticeDetailView.as_view()),
]
