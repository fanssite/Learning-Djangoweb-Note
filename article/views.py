from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn,ArticlePost
from account.models import UserInfo
from django.views.decorators.csrf import csrf_exempt
from article.forms import ArticleColumnForm, ArticlePostForm
from django.http.response import HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

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
def articlepost(req):
    if req.method=='POST':
            article_post_form=ArticlePostForm(req.POST)
            if article_post_form.is_valid():
#                 cd = article_post_form.cleaned_data
                try:
                    new_article=article_post_form.save(commit=False)
                    new_article.author = req.user
                    print(new_article.author,req.POST['column_id'])
                    new_article.column = ArticleColumn.objects.get(user=req.user,id=req.POST['column_id'])
                    new_article.save()
                    return HttpResponse('1')
                except:
                    return HttpResponse('0')
            return HttpResponse('2')
    else:
        article_post_form=ArticlePostForm()
        article_columns = ArticleColumn.objects.filter(user=req.user)   #req.user.article_column.all()  models中有个related——name参数用来查询登录用户的对应models字段Queryset
        myinfo=UserInfo.objects.get(user=req.user)
        return render(req, 'article/column/article_post.html',{'article_post_form':article_post_form,'article_columns':article_columns,'userinfo':myinfo})
    
@login_required(login_url='/account/login/')
def article_list(req):
    articles = ArticlePost.objects.filter(author=req.user)
    paginator = Paginator(articles,2)
    page = req.GET.get('page')
    myinfo=UserInfo.objects.get(user=req.user)
    try:
        current_page=paginator.page(page)
        article = current_page.object_list
    except PageNotAnInteger:
        current_page=paginator.page(1)
        article=current_page.object_list
    except EmptyPage:
        current_page=paginator.page(paginator.num_pages)
        article=current_page.object_list
    return render(req,'article/column/article_list.html',{'articles':article,'userinfo':myinfo,'page':current_page})
            
@login_required(login_url='/account/login/')                    
def article_detail(req,id,slug):
    article=get_object_or_404(ArticlePost,id=id,slug=slug)
    myinfo=UserInfo.objects.get(user=req.user)
    return render(req,'article/column/article_detail.html',{'article':article,'userinfo':myinfo})

@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def delete_article(req):
    article_id=req.POST['article_id']
    try:
        article=ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse('1')
    except:
        return HttpResponse('0')

@login_required(login_url='/account/login/')
@csrf_exempt
def edit_article(req,article_id):
    if req.method=='GET':
#         print(dir(req.user),article_id)
        article_columns = req.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={'title':article.title})
        this_article_column = article.column
        return render(req,'article/column/edit_article.html', {'article_columns':article_columns,'article':article,'this_article_form':this_article_form,'this_article_column':this_article_column})
    else:
        edit_article=ArticlePost.objects.get(id=article_id)
        try:
            edit_article.column = req.user.article_column.get(id=req.POST['column_id'])
            edit_article.title=req.POST['title']
            edit_article.body=req.POST['body']
            edit_article.save()
            return HttpResponse('1')
        except:
            return HttpResponse('2')