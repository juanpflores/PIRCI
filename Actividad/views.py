from django.shortcuts import render

# Create your views here.
def Landing(request):
    return render(request, '../../templates/landing/index.html', {})