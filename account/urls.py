#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
# from django.conf import settings

urlpatterns =[
#     url(r'login/',auth_views.login,name='user_login'),
#     url(r'^login',auth_views.login,name='user_login'),
    url(r'login',auth_views.login,
        {'template_name':'account/login.html'},
        name='user_login'),#该方法可以直接定向到account app下的login.html页面
    
    url(r'^logout',auth_views.logout,
        {'template_name':'account/logout.html'},
        name='user_logout'),
    
    url(r'^register',views.register,name='user_register'),
    
    url(r'^password_change/$',auth_views.password_change,
        {'post_change_redirect':'/account/password_change_done'},
        name='password_change'),
    
    url(r'^password_change_done',auth_views.password_change_done,
        name='password_change_done'),
    
    
    url(r'^password_reset/$',auth_views.password_reset,
        {'template_name':'account/password_reset.html',
         'email_template_name':'account/password_reset_email.html',
         'subject_template_name':'account/password_reset_subject_txt',
         'posr_reset_redirect':'account/password_reset_done'},
        name='password_reset'),
    
    url(r'^password_reset_done/$',auth_views.password_reset_done,
         {'template_name':'account/password_reset_done.html'},
        name='password_reset_done'),
   
    url(r'^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,
         {'template_name':'/account/password_reset_confirm.html',
          'posr_reset_redirect':'account/password_reset_complete'},
        name='password_reset_confirm'),
    
    url(r'^password_reset_complete/$',auth_views.password_reset_complete,
         {'template_name':'account/password_reset_complete.html'},
        name='password_reset_complete'),
    
    url(r'^myinfo/$',views.myInfo,name='myinfo'),
    
    url(r'myinfo_edit/', views.myinfo_edit, name='myinfo_edit'),
    
    url(r'^myimage/',views.my_img,name='myimage')
    
]