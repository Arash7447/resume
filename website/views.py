from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

def index_view(request) :
    context = {'name':'Arash', 'last_name':'Ghahremani','number':'09129159633','email':'Arash.sotoudeh6@gmail.com'}
    return render(request, "website/index.html",context)



