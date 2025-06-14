from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .functional_views import song_list, song_detail
# from .class_based_api_views import SongList, SongDetail
# from .class_based_mixin_views import SongList, SongDetail
# from .class_based_generic_views import SongList, SongDetail
# from .manual_generic_api_views import SongList, SongDetail, UserList, UserDetail
from .views import UserViewSet, SongViewSet, api_root

song_list = SongViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)
song_detail = SongViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

user_list = UserViewSet.as_view(
    {
        "get": "list",
    }
)
user_detail = UserViewSet.as_view({"get": "retrieve"})

# urlpatterns = [path("", song_list), path("<int:pk>", song_detail)]
# urlpatterns = [
#     path("songs/", SongList.as_view(), name="song-list"),
#     path("songs/<int:pk>", SongDetail.as_view(), name="song-detail"),
#     path("users/", UserList.as_view(), name="user-list"),
#     path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = format_suffix_patterns(
    [
        path("", api_root),
        path("songs/", song_list, name="song-list"),
        path("songs/<int:pk>", song_detail, name="song-detail"),
        path("users/", user_list, name="user-list"),
        path("users/<int:pk>", user_detail, name="user-detail"),
    ]
)
