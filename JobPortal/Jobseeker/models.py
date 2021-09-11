from django.db import models
from Employer.models import MyUser,JobPost
# Create your models here.

class JobseekerProfile(models.Model):
    user = models.OneToOneField(MyUser,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    age=models.IntegerField(default=18)
    gender_options=(("Male","Male"),("Female","Female"))
    gender=models.CharField(choices=gender_options,max_length=10)
    address=models.CharField(max_length=200)
    graduation=models.CharField(max_length=120)
    post_graduation = models.CharField(max_length=120,blank=True,null=True)
    experience=models.IntegerField(default=0)
    certifications=models.CharField(max_length=150,blank=True,null=True)
    resume=models.FileField(upload_to='files')

    def __str__(self):
        return self.name

class JobApplyModel(models.Model):
    name=models.ForeignKey(JobseekerProfile,on_delete=models.CASCADE)
    user=models.CharField(max_length=50)
    options=(("applied","applied"),("rejected","rejected"),("Under_review","Under_review"),
             ("Interview_scheduled","Interview_scheduled"))
    status=models.CharField(choices=options,max_length=75,default="applied")
    applied_job=models.ForeignKey(JobPost,on_delete=models.CASCADE)
    euser = models.CharField(max_length=120, null=True)