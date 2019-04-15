# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import blog

urlpatterns = [    

    url(r'^index/', blog.index, name="index"),
    url(r'^create/', blog.create, name="create"),
    url(r'^edit/(.+)/', blog.edit, name="edit"),      
       
    url(r'^show/(?P<page>\d*)?$', blog.show, name="show"),  
    url(r'^delete/(?P<id>\d*)?$', blog.delete, name="delete"),  
    url(r'^users/(?P<page>\d*)?$', blog.users, name="users"),
]