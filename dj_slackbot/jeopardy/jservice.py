import requests

from .models import Clue, Category


class JService:
    """
    Wrapper class for the jeopardy jservice API: https://jservice.io/
    """

    api_base_url = "http://jservice.io/api"

    def __init__(self):
        pass

    @classmethod
    def get_random_question(cls):
        response = requests.get(cls.api_base_url + "/random?count=1")
        json_data = response.json()[0]
        clue = cls.update_or_create_clue(json_data)
        return clue

    @staticmethod
    def update_or_create_clue(json_data):
        category, category_created = Category.objects.update_or_create(
            jservice_id=json_data["category"]["id"], defaults={"title": json_data["category"]["title"]},
        )
        clue, clue_created = Clue.objects.update_or_create(
            jservice_id=json_data["id"],
            defaults={
                "question": json_data["question"],
                "answer": json_data["answer"],
                "value": json_data["value"],
                "category": category,
            },
        )
        return clue
