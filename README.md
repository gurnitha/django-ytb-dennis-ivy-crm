### BUILDING CRM APPLICATION USING DJANGO V3.2

Github: https://github.com/gurnitha/django-ytb-dennis-ivy-crm


### --------------------------------------------
### 1. SETUP
### --------------------------------------------


#### 1.1 Setup venv, mysqliclient, django-environ, project and app

        new file:   .gitignore
        new file:   README.md
        new file:   apps/accounts/__init__.py
        new file:   apps/accounts/admin.py
        new file:   apps/accounts/apps.py
        new file:   apps/accounts/migrations/__init__.py
        new file:   apps/accounts/models.py
        new file:   apps/accounts/tests.py
        new file:   apps/accounts/views.py
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 1.2 Register the app to the project

        modified:   README.md
        modified:   apps/accounts/apps.py
        modified:   config/settings.py


#### 1.3 Setting up .env file and database

        modified:   README.md
        modified:   config/settings.py


#### 1.4 Create superuser

        modified:   README.md


#### 1.5 Create remote repository on Github

        Github: https://github.com/gurnitha/django-ytb-dennis-ivy-crm

        modified:   README.md


### --------------------------------------------
### 2. CREATING PAGES
### --------------------------------------------


#### 2.1 Create pages: Home, Products, Customer (VTURLs)

        modified:   README.md
        new file:   apps/accounts/templates/accounts/customer.html
        new file:   apps/accounts/templates/accounts/dashboard.html
        new file:   apps/accounts/templates/accounts/products.html
        new file:   apps/accounts/urls.py
        modified:   apps/accounts/views.py
        modified:   config/urls.py


#### 2.2 Template inheritance with base template

        modified:   README.md
        new file:   apps/accounts/templates/accounts/base.html
        modified:   apps/accounts/templates/accounts/customer.html
        modified:   apps/accounts/templates/accounts/dashboard.html
        new file:   apps/accounts/templates/accounts/navbar.html
        modified:   apps/accounts/templates/accounts/products.html


#### 2.3 Added more templates:customer_details, order_update

        modified:   README.md
        modified:   apps/accounts/templates/accounts/base.html
        new file:   apps/accounts/templates/accounts/customer_details.html
        modified:   apps/accounts/templates/accounts/dashboard.html
        modified:   apps/accounts/templates/accounts/navbar.html
        new file:   apps/accounts/templates/accounts/order_update.html
        modified:   apps/accounts/templates/accounts/products.html
        modified:   apps/accounts/urls.py
        modified:   apps/accounts/views.py