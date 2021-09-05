from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.    

class MyUserManager(BaseUserManager):
    def create_user(self, email,role,username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            role=role,
            username=username

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,role,username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            role=role,
            username=username

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email=models.EmailField(max_length=50,unique=True)
    username = models.CharField(max_length=50)
    options=(("Employer","Employer"),("Employee","Employee"),("options","options"))
    role=models.CharField(max_length=25,choices=options,default="centerhead")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_login=models.IntegerField(null=True,default=None)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role','username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class EmployerProfile(models.Model):
      overview=models.CharField(max_length=300)
      website=models.CharField(max_length=25)
      field=models.CharField(max_length=40)
      company_size=models.CharField(max_length=300)
      headquarters=models.CharField(max_length=60)
      industry_type=models.CharField(max_length=30)
      specialities=models.CharField(max_length=300)
      user=models.CharField(max_length=25)

class JobPost(models.Model):
      company=models.ForeignKey(EmployerProfile,on_delete=models.CASCADE)
      job_position=models.CharField(max_length=40)
      min_experience=models.CharField(max_length=10)
      max_experience=models.CharField(max_length=10)
      vacancies=models.CharField(max_length=10)
      location=models.CharField(max_length=40)
      salary=models.CharField(max_length=40)
      job_discription=models.CharField(max_length=100)
      candidate_profile=models.CharField(max_length=100)
      employment_type=models.CharField(max_length=50)
      education=models.CharField(max_length=100)
      myuser=models.CharField(max_length=100,null=True)

