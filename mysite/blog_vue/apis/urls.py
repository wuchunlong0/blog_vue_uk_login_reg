# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from . import blogs
from . import users
urlpatterns = [
    url(r'^index/', blogs.index, name="index"),
    url(r'^apiblogs/(?P<page>\d*)?$', blogs.apiblogs, name="apiblogs"),
    url(r'^blog/(.+)/', blogs.blog, name="blog"),                     
    url(r'^usersapi/(?P<page>\d*)?$', users.usersapi, name="usersapi"),
    url(r'^blogpage/(?P<page>\d*)?$', blogs.blogpage, name="blogpage")
]