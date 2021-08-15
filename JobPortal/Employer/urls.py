from django.urls import path
from django.shortcuts import render
from Employer import views
urlpatterns=[
        path('accounts/register',views.registartion_view,name="register"),
        path('accounts/signin',views.signin,name="signin"),
        path('accounts/signout',views.Signout,name="signout"),
        path('',lambda request:render(request,"home.html"),name="base")
]