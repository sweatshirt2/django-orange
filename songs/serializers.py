from typing import Dict
from rest_framework import serializers

from .models import Song


class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # The below config for required and allow blank is the default
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)

    def create(self, validated_data: Dict) -> Song:
        """create and return new 'Song' instance, with validated data

        Kwargs:
        validated_data -- dictionary of validated data as an input to create a 'Song' instance

        Return: a 'Song' instance
        """
        print("validated data", validated_data)
        return Song.objects.create(**validated_data)

    def update(self, instance: Song, validated_data: Dict) -> Song:
        """update and return a 'Song' instance, with the validated data

        Kwargs:
        instance -- old instance of 'Song' before update

        Return: the updated 'Song' instance
        """
        print("instance", instance)
        print("validated data", validated_data)
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance
