from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Tweet
from .api.serializers import TweetSerializer


class TweetView(APIView):
    """Handle post and get requests for tweets"""
    serializer_class = TweetSerializer

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = self.serializer_class(tweets, many=True)
        return Response(
            {
                "status": "success",
                "message": "Tweets retrieved successfully",
                "data": serializer.data
            }
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "status": "success",
                "message": "Tweet posted successfully",
                "data": serializer.data
            }
        )
