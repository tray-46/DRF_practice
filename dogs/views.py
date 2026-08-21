from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from dogs.models import Bread, Dog
from dogs.serializers import BreadSerializer, DogSerializer


# Create your views here.
class BreadListAPIView(ListAPIView):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer


class BreadRetrieveAPIView(RetrieveAPIView):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer


class BreadCreateAPIView(CreateAPIView):
    serializer_class = BreadSerializer


class BreadUpdateAPIView(UpdateAPIView):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer


class BreadDestroyAPIView(DestroyAPIView):
    queryset = Bread.objects.all()


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
