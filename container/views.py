from django.http import JsonResponse
from models import Container
from engine.models import Engine
from .services import ContainerService


def container_list(request):
    engines = Engine.objects.all()
    if not Container.objects.all().exists():
        ContainerService.create_container(engines)
        ContainerService.update_container(engines)
        return JsonResponse({'message':'success'})
    ContainerService.update_container(engines)
    return JsonResponse({'message':'created'})