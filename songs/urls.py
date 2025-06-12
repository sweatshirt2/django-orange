from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import song_list, song_detail

urlpatterns = [path("", song_list), path("<int:pk>", song_detail)]
urlpatterns = format_suffix_patterns(urlpatterns)
