from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.Landing, name='Landing'),
    url(r'register$', views.Register, name='Register'),
    url(r'newUser', views.Welcome, name='Welcome'),
    url(r'logIn$', views.LogIn, name='LogIn'),
    url(r'logInAttempt', views.LogVerify, name='LogVerify'),
    url(r'dashboard/main$',views.DashboardMain,name='DashboardMain'),
	url(r'dashboard/premios/500$',views.Premios500,name='Premios500'),
	url(r'logOut',views.LogOut,name='LogOut'),
	url(r'puntosDisponibles',views.PuntosDisp,name='PuntosDisp'),
	url(r'historial-de-puntos',views.HistPuntos,name='HistPuntos'),
	url(r'canjea500/tramites',views.Canjea500Tramites,name='Canjea500Tramites'),
	url(r'canjea500/adeudos',views.Canjea500Adeudos,name='Canjea500Adeudos'),
	url(r'canjea1000/tramites',views.Canjea1000Tramites,name='Canjea1000Tramites'),
	url(r'canjea1000/adeudos',views.Canjea1000Adeudos,name='Canjea1000Adeudos')
	]