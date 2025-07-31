from django.contrib import admin
from django.urls import path
from .views import RefreshView, LoginView, MeView


urlpatterns = [
    path("login/", LoginView.as_view(), name="authentication-endpoint"),
    path("token/refresh/", RefreshView.as_view(), name="refresh-token-endpoint"),
    path("me/", MeView.as_view(), name="me-endpoint"),
]