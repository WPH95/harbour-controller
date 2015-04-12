from image.models import Image
import datetime
import requests
from models import Container


class ContainerService(object):

    @classmethod
    def create_container(cls, engines):
        for engine in engines:
            response = requests.get(engine.url('/containers'))
            results = response.json()['results']
            for result in results:
                container = Container()
                container.uid = result['Id']
                container.image = Image.objects.get(uid=result['Image'])
                container.name = result['Name']
                container.engine = engine
                container.save()


    @classmethod
    def update_container(cls, engines):
        for engine in engines:
            data = {'exec': 'containers()'}
            response = requests.post(engine.url(), data=data)
            results = response.json()['results']
            for result in results:
                container = Container.objects.get(uid=result['Id'])
                container.command = result['Command']
                container.status = result['Status']
                container.create_at = datetime.datetime.fromtimestamp(result['Created'])
                container.save()