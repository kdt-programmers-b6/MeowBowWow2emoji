from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
import os
import shutil
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .emoji_model import emoji
from . import models
from . import apps
from PIL import Image
import base64

# Create your views here.
def main_page(request):
    
    return render(request,"web/index.html")

@csrf_exempt
def emoji_api(request):
    images=request.FILES.getlist('pet_images')
    if request.method=="POST":
        if not request.session.session_key:
            request.session.save()


        emoji_model = choice_model(request.POST.get('animal'),request.POST.get('version'))#request.POST.get('animal'),request.POST.get('version')  'Cat','V1'
        
        models.Document.objects.filter(session=request.session.session_key).delete()
        

        for image in images:
            document = models.Document(
            title=image.name,
            uploadedFile=image,
            session=request.session.session_key
            )
            document.save()

        data = models.Document.objects.filter(
            session=request.session.session_key
        ).values('uploadedFile')

        data_base64 = ""
        for d in data:
            data_base64 = emoji_model.selfie2anime(img_path=os.getcwd()+'/media/'+d['uploadedFile'])
        data_base64 = base64.b64encode(data_base64.read())
        res = JsonResponse({'img_path': data_base64.decode('utf8')})#list(data) emoji.parse_args()
        res["Access-Control-Allow-Origin"]= "*"

        return res

def choice_model(animal, version):
    return_model = ''
    if animal == 'Cat':
        if version == 'V1':# v1 => light버전
            return_model = apps.WebConfig.emoji_model_cat_v1
        else:#v2 => V1버전
            return_model = apps.WebConfig.emoji_model_cat_v2
    else:#dog
        if version == 'V1':
            return_model = apps.WebConfig.emoji_model_dog_v1
        else:#v2
            return_model = apps.WebConfig.emoji_model_dog_v2

    return return_model