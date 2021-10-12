# apps/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from apps.accounts.views import home, products, customer, customer_deatils, order_update

# Appname
app_name = 'accounts'

# Urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/', customer, name='customer'),
    path('customer/details/', customer_deatils, name='customer_deatils'),
    path('order/update/', order_update, name='order_update'),
]
