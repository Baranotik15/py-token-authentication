from django.urls import path

from user.views import CreateUserView, CreateTokenView


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", CreateUserView.as_view(), name="me"),
]

app_name = "user"
