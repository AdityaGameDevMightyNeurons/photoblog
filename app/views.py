from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.models import Images

# Create your views here.

def Home(request):
    banner_list = []
    specific_list = []
    landscape_list = []
    list_of_images = Images.objects.all()
    for i in list_of_images:
        if i.imagetype == "banner":
            banner_list.append(i.file.url)
        if i.imagetype == "specific":
            specific_list.append({"url":i.file.url,"name":i.filename})
        else:
            landscape_list.append({"url":i.file.url,"name":i.filename})
    print(banner_list)
    return render(request,"templates/home/index.html",{"banner":banner_list,"landscape":landscape_list,"specific":specific_list})

def Landscape(request):
    banner_list = []
    landscape_list = []
    list_of_images = Images.objects.all()
    for i in list_of_images:
        if i.imagetype == "banner":
            banner_list.append(i.file.url)
        if i.imagetype == "landscape":
            landscape_list.append({"url":i.file.url,"name":i.filename})
    return render(request,"templates/landscape/landscape.html",{"banner":banner_list,"landscape":landscape_list})

def Specific(request):
    banner_list = []
    specific_list = []
    list_of_images = Images.objects.all()
    for i in list_of_images:
        if i.imagetype == "banner":
            banner_list.append(i.file.url)
        if i.imagetype == "specific":
            specific_list.append({"url":i.file.url,"name":i.filename})
    return render(request,"templates/specific/specific.html",{"banner":banner_list,"specific":specific_list})


