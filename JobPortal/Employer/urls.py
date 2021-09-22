from django.urls import path
from django.shortcuts import render
from Employer import views
urlpatterns=[
         path("home",views.EmployerTotalJobApply.as_view(),name="Ehome"),
         path("profile/create",views.EmployerCreateProfileView.as_view(),name="EProfileCreate"),
         path("profile/view",views.EmployerProfileDetailView.as_view(),name="EProfileDetail"),
         path("profile/change/<int:id>",views.EmployerProfileEditView.as_view(),name="EProfileEdit"),
         path("jobpost/create",views.EmployerJobPostView.as_view(),name="EJobPostCreate"),
         path("jobpost/list",views.EmployerJobDetailView.as_view(),name="EJobPostList")
]