from django.urls import path
from . import views

appname = "asset"

urlpatterns = [
    path('recruiter/', views.recruiter, name='recruiter'),
    path('candidate/', views.candidate, name='candidate'),
    path('addjob/', views.PostAJob.as_view(), name="addjob"),
    path('alljobs/',views.AllJobsView.as_view() , name="AllJobsView"),
    path('allpostedjobs/',views.AllJobsPostedRecruiter.as_view() , name="AllJobsRecruiter"),
    path('applyforjob/<int:job_id>/',views.applyforjob,name="applyforjob"),
    path('withdrawapplication/<int:job_id>/<int:userid>/',views.withDrawApplication,name="withDrawApplication"),
    path('appliedjobs/',views.AllJobsApplied.as_view(),name="AllJobsApplied"),
    path('showallapplicants/',views.showAllApplicants,name="showAllApplicants")
]
