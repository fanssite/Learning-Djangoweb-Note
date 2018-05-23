from django.db import models
from django.contrib.auth.admin import User
# Create your models here.

class ArticleColumn(models.Model):
    user = models.ForeignKey(User,on_delete=True,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.column