from django.shortcuts import render,redirect
from Employer import forms
from django.views.generic import TemplateView,ListView,DetailView,UpdateView,CreateView,DeleteView
from Employer.models import MyUser,EmployerProfile,JobPost
from Jobseeker.models import JobApplyModel
from django.urls import reverse_lazy
# Create your views here.

class EmployerHomeView(TemplateView):
    template_name = "Employerhome.html"

class EmployerCreateProfileView(TemplateView):
    model = EmployerProfile
    form_class = forms.EmployerProfileCreateForm
    template_name = "EProfileCreation.html"
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            profile=form.save(commit=False)
            myuser=MyUser.objects.get(email=request.user)
            myuser.is_login=1
            profile.user = request.user
            profile.save()
            myuser.save()
            return redirect("Ehome")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)

class EmployerProfileDetailView(ListView):
    model= EmployerProfile
    context_object_name = "profile"
    template_name = "EmployerProfileDetail.html"
    def get_queryset(self):
        return self.model.objects.get(user=self.request.user)

class EmployerProfileEditView(UpdateView):
    model = EmployerProfile
    template_name = "EmployerProfileEdit.html"
    form_class = forms. EmployerProfileEditForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy("Ehome")

class EmployerJobPostView(TemplateView):
    model=JobPost
    template_name = "EmployerJobPostCreate.html"
    form_class=forms.EmployerJobPostCreateForm
    context = {}
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        self.context["form"] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            cdetails=EmployerProfile.objects.get(user=request.user)
            job.myuser=request.user
            job.company=cdetails
            job.save()
            return redirect("Ehome")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class EmployerJobDetailView(ListView):
    model= JobPost
    context_object_name = "jobs"
    template_name = "EmployerJobDetails.html"
    def get_queryset(self):
        return self.model.objects.filter(myuser=self.request.user)

class EmployerTotalJobApply(TemplateView):
    template_name = "Employerhome.html"
    model=JobApplyModel
    context={}
    def get(self, request, *args, **kwargs):
        apply=self.model.objects.filter(status="applied",euser=request.user).count()
        self.context["apply"]=apply
        self.context["jobapplies"]=self.model.objects.filter(status="applied",euser=request.user)
        jobposts=JobPost.objects.filter(status="created",myuser=request.user)
        self.context["jobposts"]=jobposts
        self.context["post"] = jobposts.count()
        return render(request, self.template_name, self.context)