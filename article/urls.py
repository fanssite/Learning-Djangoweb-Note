#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^article_column/$',views.article_column,name='article_column'),
    url(r'^article/rename_article_column/$',views.rename_article_column,name='rename_article_column'),
    url(r'^article/delete_article_column/$',views.delete_article_column,name='delete_article_column'),
    ]