from django.urls import path
from .views import Events

urlpatterns = [
    path("events/", Events.as_view()),
]
