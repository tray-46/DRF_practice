from django.shortcuts import render
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from dogs.pagination import Paginator
from dogs.services import convert_rub_to_usd, create_stripe_price, create_stripe_session
from users.permissions import IsModerator, IsOwner
from dogs.models import Breed, Dog
from dogs.serializers import BreedSerializer, OneBreedSerializer, DogSerializer, DogDetailSerializer, DonationSerializer


# Create your views here.
class BreedListAPIView(ListAPIView):
    queryset = Breed.objects.all().order_by("name")
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Paginator


class BreedRetrieveAPIView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = OneBreedSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class BreedCreateAPIView(CreateAPIView):
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BreedUpdateAPIView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class BreedDestroyAPIView(DestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]

@method_decorator(name="destroy", decorator=swagger_auto_schema(
    operation_description="deleting the dog"
))
class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all().order_by("name")
    serializer_class = DogSerializer
    # permission_classes = [IsAuthenticated, IsModerator]
    pagination_class = Paginator
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    filterset_fields = ('breed__name',)
    ordering_fields = ('date_born',)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DogDetailSerializer
        return DogSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action  == "create":
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        elif self.action in ["update", "partial_update", "retrieve"]:
            self.permission_classes = [IsAuthenticated, IsModerator | IsOwner]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated, ~IsModerator | IsOwner]
        return super().get_permissions()


class DonationCreateAPIView(CreateAPIView):
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer: DonationSerializer):
        donation = serializer.save(user=self.request.user)
        amount_id_usd = convert_rub_to_usd(donation.amount)
        price = create_stripe_price(amount_id_usd)
        session_id, payment_url = create_stripe_session(price)
        donation.session_id = session_id
        donation.link = payment_url
        donation.save()



