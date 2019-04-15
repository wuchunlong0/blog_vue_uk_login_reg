blog_vue_uk

前端 blog实现对数据库的增、删、改操作
 http://localhost:9000/blog_vue/index/
def index(request):
    return render(request, 'blog/index.html' , context=locals()) 
    return  HttpResponse('ok') #

创建博客 http://localhost:9000/blog_vue/create/
@login_required
def create(request):
    action='/blogapi/apiblogs/'
    redirect='/blog_vue/show/'
    return render(request,"blog/create.html", context=locals())

更新博客 http://localhost:9000/blog_vue/edit/13
def edit(request,id ):
    action='/blogapi/apiblogs/'
    redirect='/blog_vue/show/'
    return render(request,"blog/edit.html", context=locals())

显示博客 http://localhost:9000/blog_vue/show/
def show(request,page):   
    page = toInt(page) 
    return render(request,"blog/show.html",context=locals())

删除博客 http://localhost:8888/blog_vue/delete/
def delete(request,id):
    id = toInt(id)         
    Blogs.objects.filter(id = id).delete()
    return HttpResponseRedirect('/blog_vue/show/') 

显示用户 http://localhost:8888/blog_vue/users/
def users(request,page):
    page = toInt(page) 
    Users = User.objects.all() #获得数据库记录 形式  
    users_list, pageList, paginator, page = djangoPage(Users,page,PAGE_NUM)
    offset = PAGE_NUM * (page - 1)
    return render(request,"blog/user_list.html",context=locals())


