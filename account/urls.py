#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from django.conf import settings

urlpatterns =[
#     url(r'login/',auth_views.login,name='user_login'),
#     url(r'^login',auth_views.login,name='user_login'),
    url(r'login',auth_views.login,{'template_name':'account/login.html'},name='user_login'),#该方法可以直接定向到account app下的login.html页面
    url(r'^logout',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'^register',views.register,name='user_register'),
    url(r'^password_change/$',auth_views.password_change,{'post_change_redirect':'/account/password_change_done'},name='password_change'),
    url(r'^password_change_done',auth_views.password_change_done,name='password_change_done'),    
]