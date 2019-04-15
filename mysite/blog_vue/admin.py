# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from . models import Blogs,Comment
 
@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):    
    list_display = ('id','author','subject','summary','content','created_at')
 
 
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):    
#     list_display = ('id','user_id')
