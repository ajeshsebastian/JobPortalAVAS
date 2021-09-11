from django.urls import path
from django.shortcuts import render
from Jobseeker import views as jview
from Employer import views

urlpatterns=[
        path('accounts/register',jview.SeekerRegistrationView.as_view(),name="register"),
        path('',jview.SignIn.as_view(),name="signin"),
        path('accounts/signout', jview.signout, name="signout"),
        path("profile/home", jview.ProfileHomeView.as_view(), name="profilehome"),
        path("profile/create", jview.ProfileCreate.as_view(), name="profilecreate"),
        path("profile/details", jview.ViewJobseekerProfile.as_view(), name="jobseekerdetails"),
        path("profile/edit/<int:pk>", jview.UpdateProfile.as_view(), name="editprofile"),
        path("jobs", jview.JobListView.as_view(), name="alljobs"),
        path("jobs/details/<int:pk>", jview.JobDetails.as_view(), name="jobdetails"),
        path("jobs/apply/<int:id>", jview.jobapply, name="apply"),
        path("jobs/applied", jview.AppliedJobsListView.as_view(), name="appliedjobs"),
        path("jobs/applied/delete/<int:pk>", jview.CancelAppliedJob.as_view(), name="canceljob")

]