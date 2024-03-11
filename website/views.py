from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request) :
    return render(request, "website/index.html")

def fullname_view(request):
    context = {'name':'Arash', 'last_name':'Ghahremani'}
    return render (request,'website/index.html',context)

def number_email_view(request) :
    context = {'number':'09129159633','email':'Arash.sotoudeh6@gmail.com'}
    return render (request,'index.html',context)