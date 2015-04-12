from django.http import JsonResponse
import requests
from engine.models import Engine
from image.models import Image
from datetime import datetime
import json


class ImageServer(object):

    @classmethod
    def update_image(cls, engines):
        for engine in engines:
            data = {'exec': 'images()'}
            response = requests.post(engine.url(), data=data)
            results = response.json()['results']

            for result in results:
                image = Image()
                image.create_at = datetime.fromtimestamp(result['Created'])
                image.uid = result['Id']
                image.size = result['Size']
                image.virtualsize = result['VirtualSize']
                image.tag = json.dumps(result['RepoTags'])
                image.name = result['RepoTags'][0].split(':')[0]
                image.engine = engine
                if image.name == '<none>':
                    image.order = 99
                image.save()