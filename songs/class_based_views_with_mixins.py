from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

# GenericAPIView imported to provide the functionality to use the view classes as view
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Song
from .serializers import SongSerializer


class SongList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    a class to implement non id actions | Get list and Post
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request: Request) -> Response:
        """get list of 'Song' instances with a method from list mixin model

        Kwargs:
        request -- a rest framework request object

        Return: rest framework response with list of 'Song' instances
        """
        return self.list(request)

    def post(self, request: Request):
        """create a 'Song' instance and return it with create mixin model

        Kwargs:
        request -- a rest framework request object

        Return: rest framework response with a 'Song' instance
        """
        return self.create(request)


class SongDetail(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericAPIView,
):
    """
    a class to handle id related actions | Get single, Update, Delete
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get(self, request: Request, **kwargs) -> Response:
        """get a 'Song' instance with a method from retrieve model mixin

        Kwargs:
        request -- a rest framework request object

        Return: rest framework response with a 'Song' instance
        """
        return self.retrieve(request, **kwargs)

    def put(self, request: Request, **kwargs) -> Response:
        """update a 'Song' instance with a method from update model mixin and return it

        Kwargs:
        request -- a rest framework request object

        Return: rest framework response with a 'Song' instance
        """
        return self.update(request, **kwargs)

    def delete(self, request: Request, **kwargs) -> Response:
        """delete an instance of 'Song'

        Kwargs:
        request -- a rest framework request object

        Return: a rest framework response object with no content status
        """
        return self.destroy(request, **kwargs)
