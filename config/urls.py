from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/user", include("account.urls")),
    path("api/v1/company", include("company.urls")),
    path("api/v1/recruitment-notice", include("recruitment_notice.urls")),
    path("api/v1/recruitment-support", include("recruitment_support.urls")),
]
