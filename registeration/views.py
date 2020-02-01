from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("index")

def login(request):
    return HttpResponse("login")

def signup(request):
    return HttpResponse("signup")

def logout(request):
    return HttpResponse("logout")
