from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn
from account.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from article.forms import ArticleColumnForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(req):
    if req.method=='GET':
        columns = ArticleColumn.objects.filter(user=req.user)
        column_form=ArticleColumnForm()
        userinfo = UserInfo.objects.get(user=req.user)
        return render(req,'article/column/article_column.html',{'columns':columns,'userinfo':userinfo,'column_form':column_form})   
    if req.method=='POST':
        column_name = req.POST['column'].strip(' ')
        columns = ArticleColumn.objects.all().filter(user_id=req.user.id,column=column_name)  #设定当前用户和栏目名俩个条件
        if columns:
            return HttpResponse('has exited')
        elif column_name.strip(' ')=='':
            return HttpResponse('space')
        else:
            ArticleColumn.objects.create(user=req.user,column=column_name)
            return HttpResponse("1")
        
@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article_column(req):
    column_name=req.POST['column_name']
    column_id=req.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column=column_name
        line.save()
        return HttpResponse('1')
    except:
        return HttpResponse('0')
    
@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def delete_article_column(req):
    column_id=req.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('0')
