# apps/accounts/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.accounts.models import Customer, Product, Tag, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)