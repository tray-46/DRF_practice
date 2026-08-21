from rest_framework import serializers

from dogs.models import Bread, Dog


class BreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bread
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = "__all__"
