from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import RegisterUser
from .models import Usuario
from .models import Sesion
from .models import Acti
from .models import HistorialDeVisitas
from .models import HistoriaPremios
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
	
	if t is not None:
		Sesion.objects.all().delete()
		Sesion.objects.create(userTitle=t)
		Usuario.objects.create(curp=c, password=p, monedas='0', correo=e,title=t)
		return HttpResponseRedirect("./dashboard/main")
	#me = User.objects.get(username='ola')
	#return render(request, 'dashboard/main-Screen.html')
	return HttpResponseRedirect("./register")

def DashboardMain (request):
	#get the proper amount of points
	return render(request,'dashboard/main-Screen.html',{'miUsuario': Usuario.objects.filter(title= Sesion.objects.all()[0].getUser())[0]})

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
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].getCoins()
	if c>499:
		return render(request, 'dashboard/premios500.html', {'coins':c})
	return HttpResponseRedirect("../../dashboard/main")
def Premios1000 (request):
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].getCoins()
	if c>999:
		return render(request, 'dashboard/premios1000.html', {})
	return HttpResponseRedirect("../../dashboard/main")
def LogOut(request):
	Sesion.objects.all().delete()
	return HttpResponseRedirect("/")

def Canjea500Tramites(request):
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].setCoins(-500)
	HistoriaPremios.objects.create(area="Tramites>SRE", concepto="¡Felicidades! Recibiste un descuento de $100 en tu pago de pasaporte.",usuario=un)
	return render(request, 'dashboard/canjea500tramites.html',  )
def Canjea500Adeudos(request):
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].setCoins(-500)
	HistoriaPremios.objects.create(area="Adeudos>Tránsito", concepto=r"¡Felicidades! Eres acreedor a un descuento del 10% en tu próxima multa. ",usuario=un)
	return render(request, 'dashboard/canjea500adeudos.html', {})
def Canjea1000Tramites(request):
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].setCoins(-1000)
	HistoriaPremios.objects.create(area="Trámites>Tránsito", concepto="¡Vaya! Te has ganado pasar a la fila rápida la próxima vez que renueves tu tarjeta de circulación.",usuario=un)
	return render(request, 'dashboard/canjea1000tramites.html', {})
def Canjea1000Adeudos(request):
	un=Sesion.objects.all()[0].getUser()
	c=Usuario.objects.filter(title=un)[0].setCoins(-1000)
	HistoriaPremios.objects.create(area="Adeudos>SMA", concepto="¡En tu próxima verificación tendrás atención inmediata!",usuario=un)
	return render(request, 'dashboard/canjea1000adeudos.html', {})

def HistPuntos(request):
	return render(request, 'dashboard/historialPremios.html', {'posts':HistoriaPremios.objects.filter(usuario=Sesion.objects.all()[0].getUser())})

def CanjeaCodigo(request):
	return render(request, 'dashboard/canjeaCodigo.html', {})

def Add500(request):
	u=Sesion.objects.all()[0].getUser()
	Usuario.objects.filter(title=u).agregarPuntos(500)
	return HttpResponseRedirect("dashboard/main-screen.html")
def Add1000(request):
	u=Sesion.objects.all()[0].getUser()
	Usuario.objects.filter(title=u).agregarPuntos(1000)
	return HttpResponseRedirect("dashboard/main-screen.html")
def Loose500(request):
	u=Sesion.objects.all()[0].getUser()
	Usuario.objects.filter(title=u).quitarPuntos(500)
	return HttpResponseRedirect("dashboard/main-screen.html")
def Loose1000(request):
	u=Sesion.objects.all()[0].getUser()
	Usuario.objects.filter(title=u).quitarPuntos(1000)
	return HttpResponseRedirect("dashboard/main-screen.html")