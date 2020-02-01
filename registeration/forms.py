from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    category = forms.ChoiceField(choices = (('Recruiter','Recruiter'),('Job Applicant','Job Applicant')))

    class Meta:
        model = User
        fields = ('category','username','email','password1', 'password2', )
