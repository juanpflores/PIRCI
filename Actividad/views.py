from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import RegisterUser
from .models import Usuario
from .models import Sesion
from .models import Acti
from .models import HistorialDeVisitas
# Create your views here.
def Landing(request):
	Sesion.objects.all().delete()
	return render(request, 'landing/index.html', {})

def Register(request):
	return render(request, 'landing/register.html', {})

def Welcome(request):
	c=request.POST.get("myCurp")
	p=request.POST.get("myPass")
	e=request.POST.get("myEmail")
	t=request.POST.get("myTitle")
	if c is not None:
		Usuario.objects.create(curp=c, password=p, monedas='0', correo=e,title=t)
	
	#me = User.objects.get(username='ola')
	#return render(request, 'dashboard/main-Screen.html')
	return HttpResponseRedirect("dashboard/main")

def DashboardMain (request):
	#get the proper amount of points
	return render(request,'dashboard/main-Screen.html',{'miUsuario': Sesion.objects.all()[0].getUser()})

def LogIn(request):
	return render(request,'landing/logIn.html')
def LogVerify(request):
	u=request.POST.get("userN")
	us=Usuario.objects.filter(title=u)
	if us:
		for user in us:
			if user.getPass()==request.POST.get("pass"):
				Sesion.objects.all().delete()
				Sesion.objects.create(userTitle=u)
				return HttpResponseRedirect('dashboard/main')
	return HttpResponseRedirect("/logIn")

def PuntosDisp (request):
	aMostrar=[]
	#conseguir la lista de actividades
	actividades=Acti.objects.all()
	#conseguir la lista de Visitas realizadas por el usuario
	us=Sesion.objects.all()
	realizadas=HistorialDeVisitas.objects.filter(user=us[0].getUser())
	#obtener la lista de las actividades que no tengan contraparte en realizadas
	for accion in actividades:
		t=HistorialDeVisitas.objects.filter(user=us[0].getUser()).filter(evento=accion.getId())
		if not t:
			aMostrar.append(accion)

	return render(request, 'dashboard/puntosDisponibles.html', {'posts':aMostrar})

def Premios500 (request):
	return render(request, 'dashboard/premios500.html', {})

def LogOut(request):
	Sesion.objects.all().delete()
	return HttpResponseRedirect("/")

def Canjea500Tramites(request):
	return render(request, 'dashboard/canjea500tramites.html', {})
def Canjea500Adeudos(request):
	return render(request, 'dashboard/canjea500adeudoss.html', {})

def HistPuntos(request):
	return render(request, 'dashboard/canjea500adeudoss.html', {})
