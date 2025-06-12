from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .models import Song
from .serializers import SongSerializer


@csrf_exempt
def song_list(request: Response) -> JsonResponse:
    """list all songs or create a new one

    Kwargs:
    request -- ? questionable but i guess a (rest framework or http) request object

    Return: JSONResponse of list of all songs or a created song based on the request method
    """
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)

        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    if request.method == "POST":
        data = JSONParser().parse(request)
        # ? is the data argument being passed as data verbose ???
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def song_detail(request: Response, pk: int) -> HttpResponse | JsonResponse:
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
        return JsonResponse(serializer.data)

    if request.method == "PUT":
        data = JSONParser().parse(request)
        # ? why is data given to the serializer here ???
        serializer = SongSerializer(song, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, 400)

    if request.method == "DELETE":
        song.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
