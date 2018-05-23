from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn
from account.models import UserInfo

# Create your views here.
@login_required(login_url='/account/login/')
def article_column(req):
    columns = ArticleColumn.objects.filter(user=req.user)
    userinfo = UserInfo.objects.get(user=req.user)
    return render(req,'article/column/article_column.html',{'columns':columns,'userinfo':userinfo})