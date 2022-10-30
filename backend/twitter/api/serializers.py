from rest_framework import serializers
from twitter.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    """Serialize data coming from client"""

    class Meta:
        model = Tweet
        fields = ["name", "message", "timestamp"]
