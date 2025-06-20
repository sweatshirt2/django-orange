from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Song, Notification


@receiver(signal=post_save, sender=Song)
def song_created(sender, instance: Song, created, **kwargs):
    """creates notifications when songs are created

    Keyword arguments:
    instance -- an instance of the Song model
    created -- whether the instance is new

    Return: None
    """

    # Todo: handle sending notifications to subscribers when the subscription feature is added
    if created:
        Notification.objects.create(content=f"New song alert. {instance.title}!")
