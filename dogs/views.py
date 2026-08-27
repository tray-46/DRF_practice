from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from dogs.models import Breed, Dog
from dogs.serializers import BreedSerializer, OneBreedSerializer, DogSerializer, DogDetailSerializer


# Create your views here.
class BreedListAPIView(ListAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedRetrieveAPIView(RetrieveAPIView):
    queryset = Breed.objects.all()
    serializer_class = OneBreedSerializer


class BreedCreateAPIView(CreateAPIView):
    serializer_class = BreedSerializer


class BreedUpdateAPIView(UpdateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDestroyAPIView(DestroyAPIView):
    queryset = Breed.objects.all()


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    filterset_fields = ('breed__name',)
    ordering_fields = ('date_born',)
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DogDetailSerializer
        return DogSerializer
