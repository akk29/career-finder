from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from enum import Enum
from .forms import SignUpForm, LoginForm


appname = "registeration"

class ROLES(Enum):
    RECRUITER = "Recruiter"
    JOB_APPLICANT = "Job Applicant"


@login_required
def index(request):
    if request.user.profile.category == ROLES.RECRUITER:
        return redirect("/recruiter")
    elif request.user.profile.category == ROLES.JOB_APPLICANT:
        return redirect("/candidate")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        msg = None
        l = LoginForm()
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                # print(user.is_active)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        print(request.user)
                        if user.profile.category == ROLES.RECRUITER:
                            return redirect("/recruiter")
                        elif user.profile.category == ROLES.JOB_APPLICANT:
                            return redirect("/candidate")
                else:
                    msg = "wrong credentials"
                    return render(request, "login.html", {"form": l, "msg": msg})
        else:
            return render(request, "login.html", {"form": l, "msg": msg})


def signup(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.profile.category = form.cleaned_data.get("category")
                user.save()
                raw_password = form.cleaned_data.get("password1")
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                if user.profile.category == ROLES.RECRUITER:
                    return redirect("/recruiter")
                elif user.profile.category == ROLES.JOB_APPLICANT:
                    return redirect("/candidate")
        else:
            form = SignUpForm()
        return render(request, "signup.html", {"form": form})


def logoutPage(request):
    logout(request)
    return redirect("/auth/login")


def handleUserRedirectionAfterLogin(request):
    if request.user.profile.category == ROLES.RECRUITER:
        return redirect("/recruiter")
    elif request.user.profile.category == ROLES.JOB_APPLICANT:
        return redirect("/candidate")
