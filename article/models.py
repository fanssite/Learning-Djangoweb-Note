from django.db import models
from django.contrib.auth.admin import User
from django.utils import timezone
from slugify import slugify
from django.urls.base import reverse
# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User,on_delete=True,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.column
    
class ArticlePost(models.Model):
    author=models.ForeignKey(User,on_delete=True,related_name='article')
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200)
    column=models.ForeignKey(ArticleColumn,on_delete=True,related_name='article_column')
    body=models.TextField()
    created=models.DateTimeField(default=timezone.now)
    updadted=models.DateTimeField(auto_now=True)
    user_like = models.ManyToManyField(User,related_name='user_like',blank=True)
    class Meta:
        ordering=('created',)
        index_together=(('id','slug'),)
        
    def __str__(self):
        return self.title
    
    def save(self,*args,**kargs):   #重写save函数
        self.slug=slugify(self.title)
        super(ArticlePost,self).save(*args,**kargs)
        
    def get_absolute_url(self):
        return reverse("article:article_detail",args=[self.id,self.slug])
    def get_url_path(self):
        return reverse("article:list_article_detail",args=[self.id,self.slug])
