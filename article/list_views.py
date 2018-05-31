#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import ArticlePost
from account.models import UserInfo 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
def article_list(req,username=None):
    if username:
        user=User.objects.get(username=username)
        article_list=ArticlePost.objects.filter(author=user)
        try:
            userinfo = UserInfo.objects.get(user=user)
        except:
            userinfo=None
    else:
        article_list=ArticlePost.objects.all()
    paginator = Paginator(article_list,4)
    page = req.GET.get('page')
    
    try:
        current_page=paginator.page(page)
        articles = current_page.object_list
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page=paginator.page(1)
        articles=current_page.object_list
    if username:
        return    render(req,'article/list/author_article_titles.html',{'articles':articles,'page':current_page,'userinfo':userinfo,'user':user})
    else:
        return render(req,'article/list/list_article_titles.html',{'articles':articles,'page':current_page})
    
def article_detail(req,id,slug):
    myinfo=UserInfo.objects.get(user=req.user)
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(req,'article/list/article_detail.html',{'article':article})