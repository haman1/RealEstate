from django.shortcuts import render

# Create your views here.


def register(register):
	return render(request, 'accounts/register.html')


def login(login):
	return render(request, 'accounts/login.html')


def dashboard(dashboard):
	return render(request, 'accounts/dashboard.html')

