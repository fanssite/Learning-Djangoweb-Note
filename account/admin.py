from django.contrib import admin
from .models import UserProfile
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','birth','phone')
    ordering=['id',]
    class Meta:
        model = UserProfile
        fields = ('user','birth','phone')

admin.site.register(UserProfile, UserProfileAdmin)

