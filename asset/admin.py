# Register your models here.
from django.contrib import admin
from .models import Job , JobsApplication

admin.site.register(Job)
admin.site.register(JobsApplication)
