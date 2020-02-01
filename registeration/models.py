from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    CATEGORY_CHOICES = (('Recruiter','Recruiter'),('Job Applicant','Job Applicant'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    First_name = models.CharField(max_length = 15 , blank = False)
    category = models.CharField(max_length = 15 , choices = CATEGORY_CHOICES)
