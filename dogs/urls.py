from django.urls import include, path
from rest_framework.routers import SimpleRouter

from dogs import views
from dogs.apps import DogsConfig

app_name = DogsConfig.name

router = SimpleRouter()
router.register(r"dogs", views.DogViewSet, basename="dog")

urlpatterns = [
    path("", include(router.urls)),
    path("breads/", views.BreadListAPIView.as_view(), name="bread-list"),
    path("breads/<int:pk>/", views.BreadRetrieveAPIView.as_view(), name="bread-detail"),
    path("breads/create/", views.BreadCreateAPIView.as_view(), name="bread-create"),
    path("breads/<int:pk>/update/", views.BreadUpdateAPIView.as_view(), name="bread-update"),
    path("breads/<int:pk>/delete/", views.BreadDestroyAPIView.as_view(), name="bread-delete"),
]
