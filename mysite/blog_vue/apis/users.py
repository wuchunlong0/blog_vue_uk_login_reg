# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http.response import HttpResponse
from myAPI.pageAPI import djangoPage,PAGE_NUM,toInt

# http://localhost:9000/blogapi/usersapi/1
def usersapi(request,page):
    page = toInt(page)
    mylist = list(User.objects.values())[(page-1)*PAGE_NUM:page*PAGE_NUM] 
    return  JsonResponse(mylist,safe=False)
        
