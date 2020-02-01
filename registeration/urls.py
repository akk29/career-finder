from django.urls import path
from . import views

appname = "auth"

urlpatterns = [
    path('login/', views.loginPage, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout')
]
