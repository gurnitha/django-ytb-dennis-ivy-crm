# apps/accounts/forms.py

# Django modules
from django import forms

# Locals
from apps.accounts.models import Order  

# Create your forms here.

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order 
		# # Create a form with spesific fields based on the in Order model
		# fields = ['customer', 'product', 'status']
		# Go and create a form with all the fields based on the Order model
		fields = '__all__'

