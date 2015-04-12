from django.http import JsonResponse
from engine.models import Engine
from image.models import Image
from .service import ImageServer
from django.shortcuts import render



def image_list(request):
    if not Image.objects.all().exists():
        engines = Engine.objects.all()
        ImageServer.update_image(engines)

    images = Image.objects.all()
    return render(request, 'default.html', locals())

