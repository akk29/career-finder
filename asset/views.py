from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def candidate(request):
    return render(request,"candidate.html")

@login_required()
def recruiter(request):
    return render(request,"recruiter.html")
