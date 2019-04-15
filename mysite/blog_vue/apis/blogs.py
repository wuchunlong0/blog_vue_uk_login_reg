# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http.response import HttpResponse
from blog_vue.models import Testusername,Blogs,Comment
from myAPI.modelAPI import get_model_values
from django.forms.models import model_to_dict  
from myAPI.pageAPI import djangoPage,PAGE_NUM,toInt
 

#http://localhost:9000/blogapi/index/
def index(request):
    return HttpResponse('ok1')

#api  http://localhost:9000/blogapi/apiblogs/
def apiblogs(request,page):
    
    page = toInt(page)      
    if request.method == 'POST':
        cleanData = request.POST.dict()
        author = request.user
        id = cleanData.get('id', -1) 
        #print('========',id)
        subject = cleanData.get('subject', '')
        summary = cleanData.get('summary', '')
        content = cleanData.get('content', '')
        blog = Blogs.objects.filter(id=id) 
        #print('========11',blog,id)
        if blog:
            blog.update(author=author,subject=subject,summary=summary,content=content)        
        else:
            blogs = Blogs(author=author,subject=subject,summary=summary,content=content)
            blogs.save()   

    mylist = list(Blogs.objects.values().order_by('-id'))[(page-1)*PAGE_NUM:page*PAGE_NUM] 
    kvs =[{'author' : User}] #外键字典
    return  JsonResponse(list(get_model_values(mylist,kvs)),safe=False)


#api  http://localhost:9000/blogapi/blog/1
def blog(request,blog_id):
    mylist = model_to_dict(Blogs.objects.get(id=blog_id))
    return  JsonResponse(mylist,safe=False)

#api  http://localhost:9000/blogapi/blogpage/
def blogpage(request,page):
    page = toInt(page)       
    if request.method == 'POST':
        cleanData = request.POST.dict()
        author = request.user
        id = cleanData.get('id', -1) 
        subject = cleanData.get('subject', '')
        summary = cleanData.get('summary', '')
        content = cleanData.get('content', '')
        blog = Blogs.objects.filter(id=id) 
        if blog:
            blog.update(author=author,subject=subject,summary=summary,content=content)        
        else:
            blogs = Blogs(author=author,subject=subject,summary=summary,content=content)
            blogs.save()   

    mylist = list(Blogs.objects.values().order_by('-id'))  #[(page-1)*PAGE_NUM:page*PAGE_NUM] 
    kvs =[{'author' : User}] #外键字典
    mylist = list(get_model_values(mylist,kvs))
    blogs_list, pageList, paginator, page = djangoPage(mylist,page,PAGE_NUM)
    offset = PAGE_NUM * (page - 1)

    data = dict(blogs = list(blogs_list),pageList=pageList,page=page,offset=offset)
    return  JsonResponse(data,safe=True)
