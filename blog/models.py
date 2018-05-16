from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class IntergerField(models.IntegerField):
    def __init__(self,val):
        if 0<val<100:
            self.val = val
        else:
            raise ValueError('please input a positive between 0 and 100!')
        return self.val

class BlogArticles(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    
#     class Meta:
#         ordering=('-publish',)
    def __str__(self):
        return self.content
class Register(models.Model):
    name = models.CharField(max_length=8)
    email = models.EmailField(verbose_name='email address',default='XXX@example.com')
    password = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=12,unique=True)
    age = models.IntegerField()
    class Meta:
        ordering = ('name',)

