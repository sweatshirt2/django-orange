from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

# from .functional_views import song_list, song_detail
from .class_based_views import SongList, SongDetail

# urlpatterns = [path("", song_list), path("<int:pk>", song_detail)]
urlpatterns = [path("", SongList.as_view()), path("<int:pk>", SongDetail.as_view())]
urlpatterns = format_suffix_patterns(urlpatterns)
