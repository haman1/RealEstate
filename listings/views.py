from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request, 'listings/listings.html')


def listing(request):
	return render(request, 'listings/listing.html')


def search(request):
	return render(request, 'listings/search.html')