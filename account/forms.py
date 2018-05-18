#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
#页面登录表单，继承Form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#注册新用户表单，继承ModelForm,会改变数据库数据
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','email')
    def clean_pwd2(self):
        cd = self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError('passwords don\'t match')
        return cd['password2']
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth','phone')
    
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth','phone')

