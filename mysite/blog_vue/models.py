import datetime
from django.db import models
from django.contrib.auth.models import User

class Testusername(models.Model):
    name = models.CharField(max_length=20,  null=True, blank=True) #unique=True,
    password = models.CharField(max_length=20,  null=True, blank=True)         
    def __str__(self):
        return self.name

class Blogs(models.Model):            
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    summary = models.CharField(max_length=100, null=True, blank=True)
    content = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self):
        return self.author
    
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    blog_id = models.ForeignKey(Blogs, on_delete=models.PROTECT)
    content = models.CharField(max_length=500, unique=True)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)
 
#     def __init__(self, user_id, blog_id, content):
#         self.user_id = user_id
#         self.blog_id = blog_id
#         self.content = content
 
    def __repr__(self):
        return '<Comment {}>'.format(self.content)

class Animal(models.Model):    
    name = models.CharField(max_length=20)
    sound = models.CharField(max_length=20)
    def speak(self):
        return 'The %s says "%s"' % (self.name, self.sound)
    
    def __str__(self):
        return self.name
