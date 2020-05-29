from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import slack

from .models import Bot


class Events(APIView):
    def post(self, request, *args, **kwargs):

        try:
            bot = Bot.objects.get(slack_verification_token=request.data.get("token"))
        except Bot.DoesNotExist:
            return Response(status=status.HTTP_403_FORBIDDEN)

        slack_client = slack.WebClient(bot.slack_bot_user_token, timeout=30)

        # verification challenge
        if request.data.get("type") == "url_verification":
            return Response(data=request.data, status=status.HTTP_200_OK)

        # process the event if it's there
        if "event" in request.data:
            event = request.data.get("event")
            print(event)

            # ignore bot's own message
            if event.get("subtype") == "bot_message":
                return Response(status=status.HTTP_200_OK)

            # process user's message
            user = event.get("user")
            text = event.get("text")
            channel = event.get("channel")

            if "hi" in text.lower():
                bot_text = "Hi <@{}> :wave:".format(user)
                slack_client.chat_postMessage(channel=channel, text=bot_text)
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)
