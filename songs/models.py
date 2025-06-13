from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(
        "auth.User", related_name="songs", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["created"]
