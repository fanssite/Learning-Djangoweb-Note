from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserForm,UserInfoForm
from .models import UserInfo,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
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
    
def register(req):
    if req.method=='POST':
        reg_form = RegistrationForm(req.POST)
        userprofile_form = UserProfileForm(req.POST)
        if reg_form.is_valid()*userprofile_form.is_valid():
            new_user = reg_form.save(commit=False)
            cd = reg_form.cleaned_data
            new_user.set_password(cd['password'])
            new_user.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = new_user
            userprofile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponseRedirect(reverse("account:user_login"))
        else:
            return HttpResponseRedirect(reverse("account:user_register"))
    else:
        emp_user = RegistrationForm()
        emp_userprofile = UserProfileForm()
        return render(req,'account/register.html',{'form':emp_user,'profile':emp_userprofile})
 
 
 
@login_required(login_url='/account/user_login')    
def myInfo(req):
    user = User.objects.get(username=req.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(req,'account/myinfo.html',{'user':user,'userprofile':userprofile,'userinfo':userinfo})

@login_required(login_url='/account/login/')
def myinfo_edit(req):
    user = User.objects.get(username=req.user.username)
    userprofile = UserProfile.objects.get(user=req.user)
    userinfo = UserInfo.objects.get(user=req.user)
    
    if req.method=='POST':
        user_form = UserForm(req.POST)
        userprofile_form = UserProfileForm(req.POST)
        userinfo_form = UserInfoForm(req.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_rq = user_form.cleaned_data
            userprofile_rq = userprofile_form.cleaned_data
            userinfo_rq = userinfo_form.cleaned_data
            user.email = user_rq['email']
            userprofile.birth = userprofile_rq['birth']
            userprofile.phone = userprofile_rq['phone']
            userinfo.school = userinfo_rq['school']
            userinfo.company = userinfo_rq['company']
            userinfo.address = userinfo_rq['address']
            userinfo.profession = userinfo_rq['profession']
            userinfo.aboutme = userinfo_rq['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/myinfo')
    else:
        user_form = UserForm(instance=req.user)
        userprofile_form = UserProfileForm(initial={'birth':userprofile.birth,'phone':userprofile.phone})#初始化对象
        userinfo_form = UserInfoForm(initial={'school':userinfo.school,'company':userinfo.company,'address':userinfo.address,'profession':userinfo.profession,'aboutme':userinfo.aboutme})
        return render(req,'account/myinfo_edit.html',{'user_form':user_form,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form,'userinfo':userinfo})
    
    
@login_required(login_url='/account/login/') 
def my_img(req):
    if req.method == 'POST':
        img = req.POST['img']
        userinfo = UserInfo.objects.get(user=req.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(req, 'account/Imagecrop.html')
    