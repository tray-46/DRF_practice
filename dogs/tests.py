from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dogs.models import Breed, Dog
from users.models import User


# Create your tests here.
class DogTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@dogs.com", username="user", password="user")
        self.user.set_password(self.user.password)
        self.breed = Breed.objects.create(name="Лабродор", description="Очень красивая собака")
        self.dog = Dog.objects.create(name="Гром", breed=self.breed, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_dog_retrieve(self):
        """dog retrieve"""
        url = reverse("dogs:dog-detail", kwargs={"pk": self.dog.pk})

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.dog.name)

    def test_dog_create(self):
        """dog create"""
        url = reverse("dogs:dog-list")

        data = {"name": "Фантик"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), 2)

    def test_dog_update(self):
        """dog retrieve"""
        url = reverse("dogs:dog-detail", kwargs={"pk": self.dog.pk})

        data = {"name": "Гром мл."}

        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Гром мл.")

    def test_dog_delete(self):
        """dog retrieve"""
        url = reverse("dogs:dog-detail", kwargs={"pk": self.dog.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dog.objects.count(), 0)

    def test_dog_list(self):
        """dog list"""
        url = reverse("dogs:dog-list")
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.dog.pk,
                    "name": "Гром",
                    "photo": None,
                    "date_born": None,
                    "breed": self.breed.pk,
                    "owner": self.user.pk,
                    "likes": [],
                },
            ],
        }

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class BreedTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="user@dogs.com", username="user", password="user")
        self.user.set_password(self.user.password)
        self.breed = Breed.objects.create(name="Лабродор", description="Очень красивая собака", owner=self.user)
        self.dog = Dog.objects.create(name="Гром", breed=self.breed, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_breed_retrieve(self):
        """breed retrieve"""
        url = reverse("dogs:breed-detail", kwargs={"pk": self.breed.pk})

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), self.breed.name)

    def test_breed_create(self):
        """breed create"""
        url = reverse("dogs:breed-create")

        data = {"name": "Спаниель"}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Breed.objects.count(), 2)

    def test_breed_update(self):
        """breed retrieve"""
        url = reverse("dogs:breed-update", kwargs={"pk": self.breed.pk})

        data = {"name": "Лабродор_"}

        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("name"), "Лабродор_")

    def test_breed_delete(self):
        """breed retrieve"""
        url = reverse("dogs:breed-delete", kwargs={"pk": self.breed.pk})

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Breed.objects.count(), 0)

    def test_breed_list(self):
        """breed list"""
        url = reverse("dogs:breed-list")

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.breed.pk,
                        "name": self.breed.name,
                        "description": self.breed.description,
                        "owner": self.user.pk,
                    },
                ],
            },
        )
