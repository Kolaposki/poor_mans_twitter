from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp", "name"]
        verbose_name_plural = "Tweets"  # A human-readable name for the object, plural
        verbose_name = "Tweet"  # A human-readable name for the object, singular

    def __str__(self):
        return f"{self.name} tweet"
