from django.contrib import admin

# Register your models here.
from blog import models
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=('title','author','content','publish')
    list_filter = ('title','author')
    search_fields= ('title','body')
    data_hierarchy = "publish"
    ordering = ['publish','author']
admin.site.register(models.BlogArticles, BlogArticlesAdmin)

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name','password','phone_num')
admin.site.register(models.Register, RegisterAdmin)