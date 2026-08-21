from django.urls import include, path
from rest_framework.routers import SimpleRouter

from dogs import views
from dogs.apps import DogsConfig

app_name = DogsConfig.name

router = SimpleRouter()
router.register(r"", views.DogViewSet, basename="dog")

urlpatterns = [
    path("", include(router.urls)),
    path("breeds/", views.BreadListAPIView.as_view(), name="bread-list"),
    path("breeds/<int:pk>/", views.BreadRetrieveAPIView.as_view(), name="bread-detail"),
    path("breeds/create/", views.BreadCreateAPIView.as_view(), name="bread-create"),
    path("breeds/<int:pk>/update/", views.BreadUpdateAPIView.as_view(), name="bread-update"),
    path("breeds/<int:pk>/delete/", views.BreadDestroyAPIView.as_view(), name="bread-delete"),
]
