# apps/accounts/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.accounts.models import Product 

# Create your views here.

def home(request):
	return render(request, 'accounts/dashboard.html')

def products(request):
	products = Product.objects.all()
	context={
		'products':products,
	}
	return render(request, 'accounts/products.html', context)

def customer(request):
	return render(request, 'accounts/customer.html')

def customer_deatils(request):
	return render(request, 'accounts/customer_details.html')

def order_update(request):
	return render(request, 'accounts/order_update.html')