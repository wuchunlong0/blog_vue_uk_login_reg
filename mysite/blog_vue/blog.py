# -*- coding: utf-8 -*-
# from django.contrib.auth import login as auth_login 
# from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Blogs
from django.contrib.auth.models import User
from myAPI.pageAPI import djangoPage,PAGE_NUM,toInt 

# http://localhost:9000/blog_vue/index/
def index(request):
    return render(request, 'blog_vue/index.html' , context=locals()) 
    return  HttpResponse('ok') #

#创建博客 http://localhost:9000/blog_vue/create/
@login_required
def create(request):
    action='/blogapi/apiblogs/'
    redirect='/blog_vue/show/'
    return render(request,"blog_vue/create.html", context=locals())

#编辑博客 http://localhost:9000/blog_vue/edit/13
def edit(request,id ):
    action='/blogapi/apiblogs/'
    redirect='/blog_vue/show/'
    return render(request,"blog_vue/edit.html", context=locals())

#显示博客 http://localhost:9000/blog_vue/show/
def show(request,page):   
    page = toInt(page) 
    return render(request,"blog_vue/show.html",context=locals())

# http://localhost:8888/blog_vue/delete/
def delete(request,id):
    id = toInt(id)         
    Blogs.objects.filter(id = id).delete()
    return HttpResponseRedirect('/blog_vue/show/') 

# http://localhost:8888/blog_vue/users/
def users(request,page):
    page = toInt(page) 
    Users = User.objects.all() #获得数据库记录 形式  
    users_list, pageList, paginator, page = djangoPage(Users,page,PAGE_NUM)
    offset = PAGE_NUM * (page - 1)
    return render(request,"blog_vue/user_list.html",context=locals())
