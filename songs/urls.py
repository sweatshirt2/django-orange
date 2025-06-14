from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SongViewSet, UserViewSet

router = DefaultRouter()
router.register(r"songs", SongViewSet, basename="song")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [path("", include(router.urls))]
