# apps/accounts/urls.py

# Django modules
from django.urls import path

# Locals
from apps.accounts.views import (
    home, products, 
    customer,
    createOrder, updateOrder,
    deleteOrder)

# Appname
app_name = 'accounts'

# Urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk_test>/', customer, name='customer'),
    path('order/create', createOrder, name='createOrder'),
    path('order/update/<str:pk_test>/', updateOrder, name='updateOrder'),
    path('order/delete/<str:pk_test>/', deleteOrder, name='deleteOrder'),
    # path('customer/<str:pk_test>/', customer, name='customer'),
    # path('customer/deatils/', customer_deatils, name='customer_deatils'),
    # path('order/update/', order_update, name='order_update'),
]
