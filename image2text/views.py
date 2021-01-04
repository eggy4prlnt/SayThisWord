from django.shortcuts import render,HttpResponse
from django.conf import settings as djangoSettings
from django.http import JsonResponse
import pyttsx3
import hashlib

def index(request):
    return render(request, 'index.html',)

def process(request):
    if request.POST:
        engine = pyttsx3.init()
        engine.save_to_file(request.POST.get("word") , "./image2text/" + djangoSettings.STATIC_URL + "tmp/"+ hashlib.md5(request.POST.get("word").encode('utf-8')).hexdigest() +".mp3")
        engine.runAndWait()
        
        response = {
            'status':'success',
            'data': djangoSettings.STATIC_URL + "tmp/"+ hashlib.md5(request.POST.get("word").encode('utf-8')).hexdigest() +".mp3"
        }
        return JsonResponse(response)