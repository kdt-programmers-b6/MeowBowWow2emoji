from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
import os
import shutil
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt



app_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','media')
# Create your views here.
def main_page(request):
    
    return render(request,"web/index.html")

@csrf_exempt
def emoji_api(request):
    images=request.FILES.getlist('pet_images')
    if request.method=="POST":
        if not request.session.session_key:
            request.session.save()

        user_path = os.path.join(app_path,request.session.session_key)

        if os.path.isdir(user_path):
            shutil.rmtree(user_path)
        print(images)
        for image in images:
            name=os.path.join(request.session.session_key,image.name)
            FileSystemStorage().save(name,image)

    res = HttpResponse(status=200)
    res["Access-Control-Allow-Origin"]= "*"
    return res

