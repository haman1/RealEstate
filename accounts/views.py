from django.shortcuts import render,redirect

# Create your views here.


def register(request):
	if request.method == 'POST':
		print('submitted')
		return redirect('register')
	else:

		return render(request, 'accounts/register.html')


def login(request):
	return render(request, 'accounts/login.html')


def logout(request):
	return redirect('home')


def dashboard(request):
	return render(request, 'accounts/dashboard.html')

