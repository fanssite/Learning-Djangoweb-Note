from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm 
# Create your views here.
def user_login(req):
    if req.method == 'POST':
        login_form=LoginForm(req.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user:
                return HttpResponse('welcome to fanssite.top,write your sucess now')
            else:
                return HttpResponse('Sorry,your username or password is valid,please checking it')
    if req.method=='GET':
        login_form = LoginForm()
        return render(req,'account/login.html',{'form':login_form})