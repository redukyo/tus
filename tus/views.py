from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def video(request):
    return render(request, 'video.html')    