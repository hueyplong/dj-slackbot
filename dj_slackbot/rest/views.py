from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.utils import timezone
import slack

from .models import Bot
from dj_slackbot.jeopardy.jservice import JService
from dj_slackbot.jeopardy.models import Turn


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

            # ignore bot's own message
            if event.get("subtype") == "bot_message":
                return Response(status=status.HTTP_200_OK)

            # process user's message
            slack_user = event.get("user")
            text = event.get("text")
            slack_channel = event.get("channel")

            if "jep" in text.lower():
                turn, created = Turn.objects.get_or_create(
                    bot=bot, channel=slack_channel, currently_active=True, defaults={"created_by": slack_user},
                )
                if created:
                    new_clue = JService.get_random_question()
                    Turn.objects.filter(pk=turn.id).update(clue=new_clue)
                    bot_text = f"New Turn: {new_clue.category.title} for ${new_clue.value}...\n{new_clue.question}"
                else:
                    if turn.clue.answer.lower() in text.lower():
                        bot_text = f"You got it!"
                    else:
                        bot_text = f"Sorry the answer was: {turn.clue.answer}"
                    Turn.objects.filter(pk=turn.id).update(
                        currently_active=False, answered_by=slack_user, answered_at=timezone.now()
                    )

                slack_client.chat_postMessage(channel=slack_channel, text=bot_text)
                return Response(status=status.HTTP_200_OK)

            if "hi" in text.lower():
                bot_text = "Hi <@{}> :wave:".format(slack_user)
                slack_client.chat_postMessage(channel=slack_channel, text=bot_text)
                return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_200_OK)
