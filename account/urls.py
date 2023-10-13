from django.urls import path, include

from account.views import UserCreate

urlpatterns = [
    path("", UserCreate.as_view()),
]
