from django.urls import path
from recruitment_support.views import RecruitementSupportView

urlpatterns = [
    path("", RecruitementSupportView.as_view()),
]
