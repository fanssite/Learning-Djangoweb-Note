from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistrationForm,UserProfileForm
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
            return HttpResponse('Register success,congratulations!')
        else:
            return HttpResponse('Register Failed')
    else:
        emp_user = RegistrationForm()
        emp_userprofile = UserProfileForm()
        return render(req,'account/register.html',{'form':emp_user,'profile':emp_userprofile})