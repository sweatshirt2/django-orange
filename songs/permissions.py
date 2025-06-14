from typing import Union
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import Song


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to allow only the owner to mutate the 'Song'
    - anonymous users can still view
    - authenticated users can create
    - only owners can update and delete
    """

    def has_permission(self, request: Request, view: Union[APIView, ViewSet]):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated

    def has_object_permission(
        self, request: Request, view: Union[APIView, ViewSet], obj: Song
    ):
        # ? shorthand but less readability
        # return request.method in permissions.SAFE_METHODS or request.user == obj.artist

        # more readable
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.artist
