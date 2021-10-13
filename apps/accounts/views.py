# apps/accounts/views.py

# Django modules
from django.shortcuts import render, redirect

# Locals
from apps.accounts.models import Product, Order, Customer  
from apps.accounts.forms import OrderForm

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

	# 1. Use the OrderForm forms
	form = OrderForm
	# 2. If request with POST method
	if request.method == 'POST':
		# print('PRINTING THE POST:', request.POST)
		''' ----THE RESULT----
		PRINTING THE POST: 
			<QueryDict: {
				'csrfmiddlewaretoken': ['07q4sf6x7H5jbaK28qqH2IScAWprPXnoyYrAQVi70C7VE1QGLyVC0BKc1mlR46ja'], 
				'customer': ['1'], 
				'product': ['1'], 
				'status': ['Pending'], 
				'Submit': ['Submit']
			}>
		'''
		# 3. Get the inputs from the form field
		form_input = OrderForm(request.POST)
		# 4. If input is valid
		if form_input.is_valid():
			# 5. Save the input to db
			form_input.save()
			# 6. Redirect to home page
			return redirect('accounts:home')

	context = {'form':form}

	return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk_test):
	form = OrderForm
	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)


def customer_deatils(request):	
	return render(request, 'accounts/customer_details.html')


def order_update(request):
	return render(request, 'accounts/order_update.html')