from django.urls import path

from user.views import UserViewSet


urlpatterns = [
    path("register/", UserViewSet.as_view(), name="register"),
    path("login/", UserViewSet.as_view(), name="login"),
    path("me/", UserViewSet.as_view(), name="me"),
]
