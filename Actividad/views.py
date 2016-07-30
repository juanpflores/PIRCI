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
	Usuario.objects.create(curp=c, password=p, monedas='0', correo=e,title=t)
	return render(request,'landing/registerUser.html')
	

