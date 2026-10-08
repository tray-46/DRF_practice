from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView as TOPView
from rest_framework_simplejwt.views import TokenRefreshView as TRView

from users.models import User
from users.serializers import TokenObtainPairSerializer, TokenRefreshSerializer, UserCreateSerializer


# Create your views here.
class TokenObtainPairView(TOPView):
    serializer_class = TokenObtainPairSerializer


class TokenRefreshView(TRView):
    serializer_class = TokenRefreshSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer: UserCreateSerializer):
        user = serializer.save()
        user.set_password(serializer.validated_data["password"])
        user.save()
