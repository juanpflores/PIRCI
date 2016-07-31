from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Landing, name='Landing'),
    url(r'register$', views.Register, name='Register'),
    url(r'newUser', views.Welcome, name='Welcome'),
    url(r'logIn$', views.LogIn, name='LogIn'),
    url(r'logInAttempt', views.LogVerify, name='LogVerify'),
    url(r'dashboard/main$',views.DashboardMain,name='DashboardMain')
]