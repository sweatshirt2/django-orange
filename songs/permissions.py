from rest_framework import permissions

from .models import Song


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    custom permission to allow only the owner to mutate the 'Song'
    """

    def has_object_permission(self, request, view, obj: Song):
        # ? shorthand but less readability
        # return request.method in permissions.SAFE_METHODS or request.user == obj.artist

        # more readable
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.artist
