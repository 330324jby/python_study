from django.http import HttpResponse
from django.shortcuts import render
from . import models
from . import get_artical

# Create your views here.
def showIndex(request):
    return render(request,"showIndex.html")

def show_movie_name(request):
    list=models.movie_name.objects.all()
    return render(request,"showMovie.html",{"list":list})

def show_baidu_wenku(request):
    id=request.GET.get("id")   
    artical=None
    if id!=None:
        artical=models.artical.objects.filter(id=id).values();
    #print(artical)
    return render(request,"showWenKu.html",{"artical":artical[0]})

def get_baidu_wenku(request):
    returndic={}
    if len(request.GET)>0:
        url=request.GET.get("url")
        artical=get_artical.getHtml(url)
        returndic["title"]=artical[0]
        returndic["content"]=artical[1]
    return render(request,"getWenKu.html",returndic)