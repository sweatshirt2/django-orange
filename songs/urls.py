from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .functional_views import song_list, song_detail
# from .class_based_api_views import SongList, SongDetail
# from .class_based_mixin_views import SongList, SongDetail
# from .class_based_generic_views import SongList, SongDetail
from .views import SongList, SongDetail, UserList, UserDetail

# urlpatterns = [path("", song_list), path("<int:pk>", song_detail)]
urlpatterns = [
    path("songs/", SongList.as_view(), name="song-list"),
    path("songs/<int:pk>", SongDetail.as_view(), name="song-detail"),
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user-detail"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
