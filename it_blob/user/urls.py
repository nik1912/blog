from django.urls import path
from user.views import Registration, Login, logout
from django.shortcuts import redirect



urlpatterns = [
    path("signin/", Registration.as_view(), name="signin_page"),
    path("login/", Login.as_view(), name="login_page"),
    path("logout/", logout, name="logout_page"),
    path("", lambda request: redirect("/user/login/")),
]
