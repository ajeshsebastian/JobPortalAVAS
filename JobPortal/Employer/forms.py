from Employer.models import MyUser,EmployerProfile,JobPost
from Employer.admin import UserCreationForm
from django.forms import ModelForm
from django import forms

class EmployerProfileCreateForm(ModelForm):
    class Meta:
        model= EmployerProfile
        fields='__all__'
        exclude=["user"]
        widgets={
            "overview": forms.Textarea(attrs={'class': "form-control"}),
            "specialities": forms.Textarea(attrs={'class': "form-control"})
        }

class EmployerProfileEditForm(ModelForm):
    class Meta:
        model= EmployerProfile
        fields='__all__'
        exclude=["user"]
        widgets={
            "overview": forms.Textarea(attrs={'class': "form-control"}),
            "specialities": forms.Textarea(attrs={'class': "form-control"})
        }

class EmployerJobPostCreateForm(ModelForm):
    class Meta:
        model=JobPost
        fields='__all__'
        exclude=["company","myuser","options"]
        widgets={
            "job_discription":forms.Textarea(attrs={'class': "form-control"})
        }
