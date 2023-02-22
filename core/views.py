from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def home(request):
    posts = Work.objects.all()
    context={
        "posts":posts
    }
    return render(request,"index.html",context)

def category(request,pageid):
    if(request.POST):
        print(request.POST)
    else:
        print("xato")
    return HttpResponse(f"<p>{pageid}</p>")

def archive(request,year):
    if int(year) > 2023:
        redirect('404/')
    return HttpResponse(f"<p>{year}</p>")

def mickey(request):
    return HttpResponse()
def no(request):
    return render(request,"404.html")