from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("register/", views.UserCreateAPIView.as_view(), name="register"),
    path("login/", views.TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
]
