# apps/accounts/views.py

# Django modules
from django.shortcuts import render

# Locals
from apps.accounts.models import Product, Order, Customer  

# Create your views here.

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	# Total customers
	total_customers = customers.count()
	# Total orders
	total_orders = orders.count()
	# Product delivered
	delivered = orders.filter(status="Delivered").count()
	# Total pending
	pending = orders.filter(status="Pending").count()

	context = {
		'orders':orders,
		'customers':customers,
		'total_customers':total_customers,
		'total_orders':total_orders,
		'delivered':delivered,
		'pending':pending,
	}
	return render(request, 'accounts/dashboard.html', context)


def products(request):
	products = Product.objects.all()
	context={
		'products':products,
	}
	return render(request, 'accounts/products.html', context)


def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)
	orders = customer.order_set.all()
	order_count = orders.count()
	context = {
		'customer':customer, 
		'orders':orders,
		'order_count':order_count,
	}
	return render(request, 'accounts/customer.html', context)


def createOrder(request):
	return render(request, 'accounts/order_form.html')


def customer_deatils(request):	
	return render(request, 'accounts/customer_details.html')


def order_update(request):
	return render(request, 'accounts/order_update.html')