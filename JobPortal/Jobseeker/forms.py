from Employer.models import MyUser
from Employer.admin import UserCreationForm
from Jobseeker.models import JobseekerProfile
from django import forms


class SeekerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=15, widget=(
        forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "type passsword"})))
    password2 = forms.CharField(max_length=15, widget=(forms.PasswordInput(attrs={'class': "form-control"})))

    class Meta:
        model = MyUser
        fields = ["email", "role", "username", "password1", "password2"]
        widgets = {
            "email": forms.TextInput(attrs={'class': "form-control"}),
            "username": forms.TextInput(attrs={'class': "form-control"}),
            "role": forms.Select(attrs={'class': "form-select"}),
        }

class LoginForm(forms.Form):
    email=forms.CharField(max_length=150,widget=forms.EmailInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

class JobseekerProfileCreationForm(forms.ModelForm):
    class Meta:
        model=JobseekerProfile
        fields=["name","email","age","gender","address","graduation","post_graduation","experience","certifications","resume"]
        widgets={
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'age': forms.NumberInput(attrs={'class': "form-control"}),
            'gender': forms.Select(attrs={'class': "form-select"}),
            'address': forms.Textarea(attrs={'class': "form-control"}),
            'graduation': forms.TextInput(attrs={'class': "form-control"}),
            'post_graduation': forms.TextInput(attrs={'class': "form-control"}),
            'experience': forms.NumberInput(attrs={'class': "form-control"}),
            'certifications': forms.TextInput(attrs={'class': "form-control"}),
            'resume': forms.FileInput(attrs={'class': "form-control"}),
        }
        labels = {"name": "Name",
                  "resume":"Upload Resume"
                  }

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=JobseekerProfile
        fields="__all__"
