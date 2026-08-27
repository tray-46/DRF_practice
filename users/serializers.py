from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as TOPSerializer, TokenRefreshSerializer as TRSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "is_staff")


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")


class TokenObtainPairSerializer(TOPSerializer):

    @classmethod
    def get_token(cls, user: User):
        token = super().get_token(user)

        token["username"] = user.username
        token["email"] = user.email

        return token


class TokenRefreshSerializer(TRSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh_token_str =attrs["refresh_token"]
        refresh_token = RefreshToken(refresh_token_str)

        user_id = refresh_token.payload.get("user_id")
        user = User.objects.get(id=user_id)

        data["username"] = user.username
        data["email"] = user.email

        return data
