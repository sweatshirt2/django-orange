from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Song
from .serializers import SongSerializer


class SongList(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
