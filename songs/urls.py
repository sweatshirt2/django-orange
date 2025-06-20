from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SongViewSet, UserViewSet, GenreList, GenreDetail, NotificationList

router = DefaultRouter()
router.register(r"songs", SongViewSet, basename="song")
router.register(r"users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("genres", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>", GenreDetail.as_view(), name="genre-detail"),
    path("notifications", NotificationList.as_view(), name="notification-list"),
]
