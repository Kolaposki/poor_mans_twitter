from django.urls import path
from twitter.views import TweetView

urlpatterns = [
    path("tweet/", TweetView.as_view(), name="tweet"),
]
