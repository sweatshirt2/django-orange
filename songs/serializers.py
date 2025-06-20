from typing import Dict
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Song, Genre, Section


class SongSectionSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ["id", "sequence", "content", "type"]

    def get_type(self, obj: Section):
        return obj.get_type_display()


class SongSerializer(serializers.ModelSerializer):
    """
    a class to serialize our 'Song' model
    """

    sections = SongSectionSerializer(many=True)
    artist = serializers.ReadOnlyField(source="artist.username")
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="name", many=True
    )

    class Meta:
        model = Song
        fields = ["id", "title", "artist", "genres", "sections"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        sorted_sections = sorted(
            representation["sections"], key=lambda x: x["sequence"]
        )

        representation["sections"] = sorted_sections
        return representation

    def create(self, validated_data: Dict):
        sections_data = validated_data.pop("sections", [])
        genres = validated_data.pop("genres", [])

        song = Song.objects.create(**validated_data)
        song.genres.set(genres)

        for section_data in sections_data:
            Section.objects.create(song=song, **section_data)

        return song

    def update(self, instance: Song, validated_data: Dict):
        sections_data = validated_data.pop("sections", [])
        genres = validated_data.pop("genres", [])

        instance.title = validated_data.get("title", instance.title)
        instance.genres.set(genres)
        instance.save()

        instance.sections.all().delete()

        for section_data in sections_data:
            Section.objects.create(song=instance, **section_data)

        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    a class to serialize the auth 'User' model with song ownership
    """

    # songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)
    song_titles = serializers.SerializerMethodField()
    # songs = SongSerializer(many=True, read_only=True)
    # songs = serializers.SerializerMethodField()
    songs = serializers.HyperlinkedRelatedField(
        view_name="song-detail", read_only=True, many=True
    )

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "songs",
            "song_titles",
        ]

    def get_song_titles(self, obj: User):
        return [song.title for song in obj.songs.all()]

    # def get_songs(self, obj: User):
    #     return [{"id": song.id, "title": song.title} for song in obj.songs.all()]


class GenreSerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ["id", "name", "songs"]

    def get_songs(self, obj: Genre):
        return [song.title for song in obj.songs.all()]
