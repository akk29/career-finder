from django.urls import path
from registeration import views

appname = "auth"

urlpatterns = [
    path('login/', views.loginPage, name='index'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutPage, name='logout'),
    #path('handleUserRedirectionAfterLogin/',views.handleUserRedirectionAfterLogin,name='handleUserRedirectionAfterLogin')
]
