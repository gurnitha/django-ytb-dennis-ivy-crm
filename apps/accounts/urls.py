# apps/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from apps.accounts.views import home, products, customer

# Appname
app_name = 'accounts'

# Urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/', customer, name='customer'),
]
