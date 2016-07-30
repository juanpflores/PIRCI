from django.shortcuts import render

# Create your views here.
def Landing(request):
    return render(request, 'landing/index.html', {})
def Register(request):
	return render(request, 'landing/register.html', {})