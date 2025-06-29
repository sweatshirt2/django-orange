from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Song
from .serializers import SongSerializer


@api_view(["GET", "POST"])
def song_list(request: Request, format=None) -> Response:
    """list all songs or create a new one

    Kwargs:
    request -- ? questionable but i guess a (rest framework or http) request object

    Return: JSONResponse of list of all songs or a created song based on the request method
    """
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        # ? is the data argument being passed as data verbose ???
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def song_detail(request: Request, pk: int, format=None) -> Response:
    """actions that require the id of the song (i.e: find-one, update, delete)

    Kwargs:
    request -- ? questionable but i guess a (rest framework or http) request object

    Return: JSONResponse
    """

    # !
    # Keyword argument shortcut requires Python 3.14 or newerPylance
    # ? what does that even mean ???

    try:
        song = Song.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # ? why is data not given to the serializer here ???
        serializer = SongSerializer(song)
        return Response(serializer.data)

    if request.method == "PUT":
        # ? why is data given to the serializer here ???
        serializer = SongSerializer(song, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, 400)

    if request.method == "DELETE":
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
