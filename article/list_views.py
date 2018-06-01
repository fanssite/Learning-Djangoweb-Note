#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import ArticlePost
from account.models import UserInfo 
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http.response import HttpResponse

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

@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def like_article(req):
    article_id=req.POST.get("id")
    action = req.POST.get("action")
    if article_id and action:
        try:
            article = ArticlePost.objects.get(id=article_id)
            if action=='like':
                article.user_like.add(req.user)
                return HttpResponse('1')
            else:
                article.user_like.remove(req.user)
                return HttpResponse('0')
        except:
            return HttpResponse('no')