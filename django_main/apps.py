from django.apps import AppConfig
# from django_main.domain.repositories import
import requests
import json


class DjangoMainConfig(AppConfig):
    data_url: str = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"

    name = 'django_main'

    def ready(self):
        request = self.requests.get(self.url)
        request_data = json.loads(request.text)