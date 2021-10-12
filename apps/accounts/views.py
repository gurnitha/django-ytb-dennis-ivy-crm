# apps/accounts/views.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'accounts/dashboard.html')

def products(request):
	return render(request, 'accounts/products.html')

def customer(request):
	return render(request, 'accounts/customer.html')

def customer_deatils(request):
	return render(request, 'accounts/customer_details.html')

def order_update(request):
	return render(request, 'accounts/order_update.html')