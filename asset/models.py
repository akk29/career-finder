from __future__ import unicode_literals
from django.db import models
from registeration.models import Profile

class Jobs(models.Model):
    title = models.CharField(max_length = 150 , blank = False)
    description = models.CharField(max_length = 150 , blank = False)
    location = models.CharField(max_length = 150 , blank = False)
    createdBy = models.ForeignKey(Profile ,on_delete = models.CASCADE)
