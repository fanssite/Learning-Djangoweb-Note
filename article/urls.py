#!/usr/bin/env python
# -*- coding:utf-8 -*-
from . import views
from django.urls.conf import path

urlpatterns = [
    path('article_column/',views.article_column,name='article_column'),
    path('article/rename_article_column/',views.rename_article_column,name='rename_article_column'),
    path('article/delete_article_column/',views.delete_article_column,name='delete_article_column'),
    path('article_post/',views.articlepost,name='article_post'),
    path('article_list/',views.article_list,name='article_list'),
    path('article_detail/<int:id>/<slug:slug>/',views.article_detail,name='article_detail'),
    path('edit_article/<int:article_id>/',views.edit_article,name='edit_article'),
    path('del_article/',views.delete_article,name='del_article'),
    ]