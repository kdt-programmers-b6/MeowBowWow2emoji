from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
import os
import shutil
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from .emoji_model import emoji
from . import models
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


        path , arg_dict = ARG(request.POST.get('animal'),request.POST.get('version'))
        emoji_model = emoji.Emoji(path, arg_dict)
        models.Document.objects.filter(session=request.session.session_key).delete()
        

        for image in images:
            document = models.Document(
            title=image.name,
            uploadedFile=image,
            session=request.session.session_key
            )
            document.save()
            #document.target_session(request.session.session_key)
            #name=os.path.join(request.session.session_key,image.name)
            #FileSystemStorage().save(name,image)
            #data.append(os.path.join('http://3.26.152.53/media',name))

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

def ARG(animal, version):
    path = os.getcwd()+'/web/emoji_model/checkpoint/'
    arg_dict = emoji.parse_args()
    
    if animal == 'Cat':
        if version == 'V1':# v1 => light버전
            path += 'UGATIT_CAT_DOWN/UGATIT_light.model-700000'
            arg_dict['light']=True
            arg_dict['ch']= 64
        else:#v2 => V1버전
            path += 'UGATIT_CAT_V1/UGATIT.model-920000'
    else:#dog
        if version == 'V1':
            path += 'UGATIT_DOG_V1/UGATIT.model-810000'
        else:#v2
            path += 'UGATIT_DOG_V2/UGATIT.model-640000'

    return path, arg_dict