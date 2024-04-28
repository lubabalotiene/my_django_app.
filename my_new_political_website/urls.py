"""
URL configuration for my_new_political_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# political_website/urls.py
from django.contrib import admin
from django.urls import path, include
from my_new_combrate import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_new_combrate/', views.my_new_combrate_details, name='my_new_combrate_detail'),
    path('', views.home_view, name='home'),  
    path('about/', views.about_view, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
]

