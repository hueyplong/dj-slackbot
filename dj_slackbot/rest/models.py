from django.db import models


class Bot(models.Model):
    slack_client_id = models.CharField(max_length=100)
    slack_client_secret = models.CharField(max_length=100)
    slack_verification_token = models.CharField(max_length=100)
    slack_bot_user_token = models.CharField(max_length=100)
