from django.urls import path
from .views import song_list, song_detail

urlpatterns = [path("", song_list), path("<int:pk>", song_detail)]
