# from the class based generic views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

from .models import Song
from .serializers import SongSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(["GET"])
def api_root(request: Request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "songs": reverse("song-list", request=request, format=format),
        }
    )


class SongList(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer: SongSerializer):
        serializer.save(artist=self.request.user)


class SongDetail(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
