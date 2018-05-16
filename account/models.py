from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=True)
    birth = models.DateTimeField(blank=True,null=True)
    phone = models.CharField(max_length=11,null=True)
    def __str__(self):
        return 'user {0}'.foramt(self.user.username)