from rest_framework import serializers

from dogs.models import Breed, Dog, Donation
from dogs.validators import WordsValidator, validate_forbidden_words


class BreedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators=[WordsValidator()])
    name = serializers.CharField(validators=[validate_forbidden_words])

    class Meta:
        model = Dog
        fields = "__all__"


class DogDetailSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    breed_count = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = ("name", "breed", "date_born", "breed_count", "likes")

    def get_breed_count(self, obj) -> int:
        if obj.breed:
            count = obj.breed.dog_set.count()
            return count
        return 0


class OneBreedSerializer(serializers.ModelSerializer):
    # dogs = DogSerializer(many=True, source="dog_set")
    dogs = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = "__all__"

    def get_dogs(self, obj) -> list[str]:
        return [dog.name for dog in obj.dog_set.all()]


class DonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donation
        fields = "__all__"
