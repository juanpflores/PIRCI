from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import RegisterUser
from .models import Usuario

# Create your views here.
def Landing(request):
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
	#usuario=request.POST.get("myTitle")
	return render(request,'dashboard/main-Screen.html')

def LogIn(request):
	return render(request,'landing/logIn.html')
def LogVerify(request):
	
	us=Usuario.objects.filter(title=request.POST.get("userN"))
	if us:
		for user in us:
			if user.getPass()==request.POST.get("pass"):
				return HttpResponseRedirect('dashboard/main')
	return HttpResponseRedirect("/logIn")
