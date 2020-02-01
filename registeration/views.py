from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm

appname = "registeration"

def index(request):
    return HttpResponse("index")

def loginPage(request):
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.category = form.cleaned_data.get('category')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            if(user.profile.category == ''):
                pass
            return redirect("/")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{'form' : form})

def logout(request):
    return HttpResponse("logout")
