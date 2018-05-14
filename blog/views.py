from django.shortcuts import render,redirect

# Create your views here.
from blog.models import BlogArticles,Register
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request, 'blog/title.html',{"blogs":blogs})
def blog_article(request,aid):
    print(aid)
    article = BlogArticles.objects.get(id=aid)
    return render(request, 'blog/content.html',{'article':article})
def Sign_in(request):
    if request.method=='GET':
        reg = Register()
        return render(request,'blog/register.html',{'form':reg})
    if request.method=='POST':
        form = Register(request.POST)
        if form.is_valid():
            post = form.cleaned_data
            name = post.get('user')
            email = post.get('email')
            password = post.get('password')
            phone_num = post.get('phone_num')
            age = post.get('age')
            Register.objects.create(name=name,password=password,email=email,phone_num=phone_num,age=age)
            return redirect('blog/register.html')
        else:
            errors = form.errors
    return render(request,'blog/register.html',{'form':form})