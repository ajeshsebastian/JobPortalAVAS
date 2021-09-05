from django.shortcuts import render,redirect
from Employer import forms
from django.views.generic import TemplateView,ListView,UpdateView,CreateView
from Employer.models import MyUser
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from Jobseeker import forms
from Jobseeker.models import JobseekerProfile
from django.http import HttpResponse,Http404,HttpResponseRedirect
import os

# Create your views here.

class SeekerRegistrationView(CreateView):
    model=MyUser
    form_class=forms.SeekerRegistrationForm
    template_name="registration.html"
    success_url = reverse_lazy("signin")

class SignIn(TemplateView):
    template_name = "signin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.LoginForm()
        return context

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                print("success")
                login(request, user)
                if request.user.role == "Employee":
                    return redirect("profilehome")
                elif request.user.role == "Employer":
                    return render(request,"EmployerBaseHome.html")
                else:
                    return redirect("register")
            else:
                context = {"form": form}
                return render(request, self.template_name, context)

class ProfileCreate(CreateView):
    template_name = "jobseeker_profile_create.html"
    form_class = forms.JobseekerProfileCreationForm
    model = JobseekerProfile

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user=request.user
            MyUser.objects.filter(email=request.user).update(is_login=1)
            profile.save()
            return redirect("profilehome")
        else:
            return render(request,"jobseeker_profile_create.html",{"form":form})


class ProfileHomeView(ListView):
    model = MyUser
    template_name = "profile_home.html"
    context_object_name = "home"
    def get_queryset(self):
        return MyUser.objects.get(email=self.request.user)


def download(request,path,id):
    file_path=os.path.join('files',path,id)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/resume")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    return Http404


class ViewJobseekerProfile(ListView):
    model=JobseekerProfile
    template_name = "jobseeker_profile_view.html"
    context_object_name = "profile"
    def get_queryset(self,):
        return JobseekerProfile.objects.get(user=self.request.user)


class UpdateProfile(UpdateView):
    model=JobseekerProfile
    template_name = "editprofile.html"
    form_class = forms.JobseekerProfileCreationForm
    success_url =reverse_lazy ("jobseekerdetails")

def signout(request):
    logout(request)
    return redirect("signin")