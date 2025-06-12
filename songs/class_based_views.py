from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Song
from .serializers import SongSerializer


class SongList(APIView):
    """
    A class to implement actions that do not require id
    """

    def get(self, request: Request, format=None) -> Response:
        """get list of songs

        Kwargs:
        request -- a rest framework request object (wraps the http request and easier to access properties)

        Return: a rest framework response object with list of songs
        """
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

    def post(self, request: Request, format=None) -> Response:
        """post a song

        Kwargs:
        request -- a rest framework request object

        Return: a rest framework response object with the created song
        """
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongDetail(APIView):
    def get_object(self, pk: int) -> Song:
        """get the object to make sure it exists and use it on the actions in other instance methods

        Kwargs:
        pk -- the primary key of the object

        Return: the requested object by it's primary key
        """
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request: Request, pk: int, format=None) -> Response:
        """get a single instance of 'Song' by it's primary key

        Kwargs:
        request -- a rest framework request object

        Return: a rest framework response object with the requested instance of 'Song'
        """
        song = self.get_object(pk)
        serializer = SongSerializer(song)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None) -> Response:
        """update and return an instance of 'Song'

        Kwargs:
        request -- a rest framework request object

        Return: a rest framework response object with the updated instance of 'Song'
        """
        song = self.get_object(pk)
        serializer = SongSerializer(song, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request: Request, pk: int, format=None) -> Response:
        """delete an instance of 'Song'

        Kwargs:
        request -- a rest framework request object

        Return: a rest framework response object with no content status
        """
        song = self.get_object(pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
