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

# Create your views here.
def main_page(request):
    
    return render(request,"web/index.html")

@csrf_exempt
def emoji_api(request):
    images=request.FILES.getlist('pet_images')
    if request.method=="POST":
        if not request.session.session_key:
            request.session.save()

        path , arg_dict = ARG('cat','v1')
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

        img_path_data = ""
        for d in data:
            img_path_data = emoji_model.selfie2anime(img_path=os.getcwd()+'/media/'+d['uploadedFile'])
        
        res = JsonResponse({'img_path': "http://13.210.122.72/"+img_path_data})#list(data) emoji.parse_args()
        res["Access-Control-Allow-Origin"]= "*"
        print(os.getcwd())
        return res

def ARG(animal, version):
    path = os.getcwd()+'/web/emoji_model/checkpoint/'
    arg_dict = emoji.parse_args()
    if animal == 'cat':
        path += 'UGATIT_CAT_DOWN/UGATIT_light.model-700000'
    else:
        path += 'UGATIT_DOG_DOWN/UGATIT_light.model-700000'
    if version == 'v1':
        arg_dict['light']=True
        arg_dict['epoch']=80
        arg_dict['iteration']=1000 
        arg_dict['batch_size']=1
        arg_dict['print_freq']=1000
        arg_dict['save_freq']=1000
        arg_dict['decay_flag']=True
        arg_dict['decay_epoch']=50
        arg_dict['lr']=0.0001
        arg_dict['GP_ld']=10
        arg_dict['adv_weight']=1
        arg_dict['cycle_weight']= 10
        arg_dict['identity_weight']= 10
        arg_dict['cam_weight']= 1000
        arg_dict['gan_type']= 'lsgan'
        arg_dict['ch']= 64
        arg_dict['n_res']= 4
        arg_dict['n_dis']= 6
        arg_dict['n_critic']= 1
        arg_dict['sn']= True
        arg_dict['img_size']=256
        arg_dict['img_ch']=3
        arg_dict['augment_flag'] = True
    elif version == 'v2':
        arg_dict['light']=True
        arg_dict['epoch']=80
        arg_dict['iteration']=1000 
        arg_dict['batch_size']=1
        arg_dict['print_freq']=1000
        arg_dict['save_freq']=1000
        arg_dict['decay_flag']=True
        arg_dict['decay_epoch']=50
        arg_dict['lr']=0.0001
        arg_dict['GP_ld']=10
        arg_dict['adv_weight']=1
        arg_dict['cycle_weight']= 10
        arg_dict['identity_weight']= 10
        arg_dict['cam_weight']= 1000
        arg_dict['gan_type']= 'lsgan'
        arg_dict['ch']= 64
        arg_dict['n_res']= 4
        arg_dict['n_dis']= 6
        arg_dict['n_critic']= 1
        arg_dict['sn']= True
        arg_dict['img_size']=256
        arg_dict['img_ch']=3
        arg_dict['augment_flag'] = True
    return path, arg_dict