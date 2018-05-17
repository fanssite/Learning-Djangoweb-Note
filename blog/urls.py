'''
Created on 2018年5月10日

@author: admin
'''
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.blog_title,name='blog_title'),
    url(r'article_id(?P<aid>\d{1,4})/',views.blog_article,name='blog_article')
]