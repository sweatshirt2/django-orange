from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Song
from .serializers import UserSerializer, SongSerializer
from .permissions import IsOwnerOrReadOnly


@api_view(["GET"])
def api_root(request: Request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "songs": reverse("song-list", request=request, format=format),
        }
    )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A class that performs Listing many and Getting a single instance with ReadOnlyModelViewSet inheritance
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class SongViewSet(viewsets.ModelViewSet):
    """
    A class that performs all actions with ModelViewSet inheritance
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer: SongSerializer):
        serializer.save(artist=self.request.user)
