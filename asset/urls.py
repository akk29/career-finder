from django.urls import path
from . import views

appname = "asset"

urlpatterns = [
    path('recruiter/', views.recruiter, name='recruiter'),
    path('candidate/', views.candidate, name='candidate'),
]
