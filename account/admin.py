from django.contrib import admin
from .models import UserProfile,UserInfo
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','birth','phone')
    ordering=['id',]
    
        
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('id','user','school','company','profession','address','aboutme','photo')
    ordering=['id',]
    list_filter=('school','profession','company')
    
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserInfo,UserInfoAdmin)

