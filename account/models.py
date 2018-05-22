from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=True)
    birth = models.DateTimeField(blank=True,null=True)
    phone = models.CharField(max_length=11,null=True)
    def __str__(self):
        return 'user {0}'.foramt(self.user.username)
        return '{0}'.format(self.user.username)

class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=True)
    address = models.CharField(max_length=100,blank=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    def __str__(self):
        return 'user:{0}'.format(self.user.username)