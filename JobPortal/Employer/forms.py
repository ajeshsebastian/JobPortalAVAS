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
            "specialities": forms.Textarea(attrs={'class': "form-control"}),
            "website": forms.TextInput(attrs={'class': "form-control"}),
            "field": forms.TextInput(attrs={'class': "form-control"}),
            "company_size": forms.TextInput(attrs={'class': "form-control"}),
            "headquarters": forms.TextInput(attrs={'class': "form-control"}),
            "industry_type": forms.TextInput(attrs={'class': "form-control"}),
            "company_name": forms.TextInput(attrs={'class': "form-control"}),
        }

class EmployerProfileEditForm(ModelForm):
    class Meta:
        model= EmployerProfile
        fields='__all__'
        exclude=["user"]
        widgets={
            "overview": forms.Textarea(attrs={'class': "form-control"}),
            "specialities": forms.Textarea(attrs={'class': "form-control"}),
            "website": forms.TextInput(attrs={'class': "form-control"}),
            "field": forms.TextInput(attrs={'class': "form-control"}),
            "company_size": forms.TextInput(attrs={'class': "form-control"}),
            "headquarters": forms.TextInput(attrs={'class': "form-control"}),
            "industry_type": forms.TextInput(attrs={'class': "form-control"}),
            "company_name": forms.TextInput(attrs={'class': "form-control"}),
        }

class EmployerJobPostCreateForm(ModelForm):
    class Meta:
        model=JobPost
        fields='__all__'
        exclude=["company","myuser","options","status"]
        widgets={
            "job_discription":forms.Textarea(attrs={'class': "form-control"}),
            "job_position": forms.TextInput(attrs={'class': "form-control"}),
            "min_experience": forms.TextInput(attrs={'class': "form-control"}),
            "max_experience": forms.TextInput(attrs={'class': "form-control"}),
            "vacancies": forms.TextInput(attrs={'class': "form-control"}),
            "location": forms.TextInput(attrs={'class': "form-control"}),
            "salary": forms.TextInput(attrs={'class': "form-control"}),
            "candidate_profile": forms.TextInput(attrs={'class': "form-control"}),
            "employment_type": forms.TextInput(attrs={'class': "form-control"}),
            "education": forms.TextInput(attrs={'class': "form-control"}),
        }
