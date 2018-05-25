from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn
from account.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from article.forms import ArticleColumnForm, ArticlePostForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST

# Create your views here.
@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(req):
    if req.method=='GET':
        columns = ArticleColumn.objects.filter(user=req.user).order_by('created')
        column_form=ArticleColumnForm()
        userinfo = UserInfo.objects.get(user=req.user)
        return render(req,'article/column/article_column.html',{'columns':columns,'userinfo':userinfo,'column_form':column_form})   
    if req.method=='POST':
        column_name = req.POST['column'].strip(' ')
        columns = ArticleColumn.objects.all().filter(user_id=req.user.id,column=column_name)  #设定当前用户和栏目名俩个条件
        if columns:
            return HttpResponse('0')
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
        print(type(line))
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
    
@login_required(login_url='/account/login/')
@csrf_exempt
def ArticlePost(req):
    if req.method=='POST':
            article_post_form=ArticlePostForm(req.POST)
            print(article_post_form)
            if article_post_form.is_valid():
                cd = article_post_form.cleaned_data
                print(cd)
                try:
                    new_article=article_post_form.save(commit=False)
                    new_article.author = req.user
                    new_article.column = req.user.article_column.get(id=req.POST['coulmn_id'])
                    new_article.save()
                    return HttpResponse('1')
                except:
                    return HttpResponse('0')
            return HttpResponse('2')
    else:
        article_post_form=ArticlePostForm()
        article_columns = ArticleColumn.objects.filter(user=req.user)   #req.user.article_column.all()  models中有个related——name参数用来查询登录用户的对应models字段Queryset
        return render(req, 'article/column/article_post.html',{'article_post_form':article_post_form})
        
        
                    
                    