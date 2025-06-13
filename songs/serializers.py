from typing import Dict
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Song


# ? Generic serializer
# class SongSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     # The below config for required and allow blank is the default
#     title = serializers.CharField(required=True, allow_blank=False, max_length=100)

#     def create(self, validated_data: Dict) -> Song:
#         """create and return new 'Song' instance, with validated data

#         Kwargs:
#         validated_data -- dictionary of validated data as an input to create a 'Song' instance

#         Return: a 'Song' instance
#         """
#         print("validated data", validated_data)
#         return Song.objects.create(**validated_data)

#     def update(self, instance: Song, validated_data: Dict) -> Song:
#         """update and return a 'Song' instance, with the validated data

#         Kwargs:
#         instance -- old instance of 'Song' before update

#         Return: the updated 'Song' instance
#         """
#         print("instance", instance)
#         print("validated data", validated_data)
#         instance.title = validated_data.get("title", instance.title)
#         instance.save()
#         return instance


class SongSerializer(serializers.ModelSerializer):
    """
    a class to serialize our 'Song' model
    """

    artist = serializers.ReadOnlyField(source="artist.username")

    class Meta:
        model = Song
        fields = ["id", "title", "artist"]


class UserSerializer(serializers.ModelSerializer):
    """
    a class to serialize the auth 'User' model with song ownership
    """

    # songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)
    # song_titles = serializers.SerializerMethodField()
    # songs = SongSerializer(many=True, read_only=True)
    songs = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "songs",
            # "song_titles",
        ]

    # def get_song_titles(self, obj: User):
    #     return [song.title for song in obj.songs.all()]

    def get_songs(self, obj: User):
        return [{"id": song.id, "title": song.title} for song in obj.songs.all()]
