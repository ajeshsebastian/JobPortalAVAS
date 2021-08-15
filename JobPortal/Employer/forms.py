from Employer.models import MyUser
from Employer.admin import UserCreationForm
from django import forms


class RegistrationForm(UserCreationForm):
      password1 = forms.CharField(max_length=15, widget=(forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "type passsword"})))
      password2 = forms.CharField(max_length=15, widget=(forms.PasswordInput(attrs={'class': "form-control"})))
      class Meta:
          model=MyUser
          fields=["email","role","username","password1","password2"]
          widgets={
            "email": forms.TextInput(attrs={'class': "form-control"}),
            "username":forms.TextInput(attrs={'class': "form-control"}),
            "role":forms.Select(attrs={'class': "form-select"}),
          }
class SigninForm(forms.Form):
    email=forms.CharField(max_length=150)
    password=forms.CharField(widget=forms.PasswordInput())