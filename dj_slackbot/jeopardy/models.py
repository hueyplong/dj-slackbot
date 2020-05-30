from django.db import models
from dj_slackbot.rest.models import Bot


class Clue(models.Model):
    jservice_id = models.IntegerField(blank=False, null=False, unique=True, db_index=True)
    question = models.TextField(blank=False, null=False)
    answer = models.CharField(max_length=255, blank=False, null=False)
    value = models.PositiveIntegerField(blank=False, null=False, default=200)
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.question


class Category(models.Model):
    jservice_id = models.IntegerField(blank=False, null=False, unique=True, db_index=True)
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.title


class Turn(models.Model):
    bot = models.ForeignKey(Bot, blank=False, null=False, on_delete=models.CASCADE)
    clue = models.ForeignKey(Clue, blank=False, null=True, on_delete=models.SET_NULL)
    channel = models.CharField(max_length=100, blank=False, null=False)
    created_by = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_by = models.CharField(max_length=100, blank=False, null=False)
    answered_at = models.DateTimeField(null=True)
    currently_active = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.channel
