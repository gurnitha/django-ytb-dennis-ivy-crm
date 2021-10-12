# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # Accounts
    path('', include('apps.accounts.urls', namespace='accounts')),

    # Admin
    path('admin/', admin.site.urls),

]
