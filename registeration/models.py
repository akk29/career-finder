from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    CATEGORY_CHOICES = (('Recruiter','Recruiter'),('Job Applicant','Job Applicant'))
    category = models.CharField(max_length = 15 , choices = CATEGORY_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key = True)
    First_name = models.CharField(max_length = 15 , blank = False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
