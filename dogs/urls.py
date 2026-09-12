from django.urls import include, path
from rest_framework.routers import SimpleRouter

from dogs import views
from dogs.apps import DogsConfig

app_name = DogsConfig.name

router = SimpleRouter()
router.register("", views.DogViewSet, basename="dog")

urlpatterns = [
    path("breeds/", views.BreedListAPIView.as_view(), name="breed-list"),
    path("breeds/<int:pk>/", views.BreedRetrieveAPIView.as_view(), name="breed-detail"),
    path("breeds/create/", views.BreedCreateAPIView.as_view(), name="breed-create"),
    path("breeds/<int:pk>/update/", views.BreedUpdateAPIView.as_view(), name="breed-update"),
    path("breeds/<int:pk>/delete/", views.BreedDestroyAPIView.as_view(), name="breed-delete"),

    path("donations/", views.DonationCreateAPIView.as_view(), name="donations"),

    path("", include(router.urls)),
]
