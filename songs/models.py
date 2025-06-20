from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(
        "auth.User", related_name="songs", on_delete=models.CASCADE
    )
    genres = models.ManyToManyField(Genre, related_name="songs")

    class Meta:
        ordering = ["created"]


class SectionType(models.TextChoices):
    CHORUS = "Ch", "Chorus"
    VERSE = "Vs", "Verse"
    BRIDGE = "Bg", "Bridge"
    HOOK = "Hk", "Hook"


class Section(models.Model):
    song = models.ForeignKey(Song, related_name="sections", on_delete=models.CASCADE)
    sequence = models.IntegerField(validators=[MinValueValidator(1)])
    content = models.TextField()
    type = models.CharField(
        max_length=2, choices=SectionType.choices, default=SectionType.VERSE
    )


class Notification(models.Model):
    content = models.TextField()
