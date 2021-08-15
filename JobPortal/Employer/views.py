from django.shortcuts import render,redirect
from Employer import forms
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from Employer.models import MyUser
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
# Create your views here.
def registartion_view(request):
    form=forms.RegistrationForm()
    context={'form':form}
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            context={'form':form}
            return render(request, "registration.html", context)
    return render(request,"registration.html",context)
# class RegistrationView(CreateView):
#     model=MyUser
#     form_class=forms.RegistrationForm
#     template_name="registration.html"
#     success_url = reverse_lazy("signin")

def signin(request):
    form=forms.SigninForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(request,email=email,password=password)
            if user:
                print("success")
                login(request,user)         
                return redirect("base")
            else:
                context={"form":form}
                return render(request,"login.html",context)
    return render(request,"login.html",context)

def Signout(request):
    logout(request)
    return redirect("signin")
