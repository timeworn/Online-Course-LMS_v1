"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

    Password Reset Confirm
    account/ login/ [name='login']
    account/ logout/ [name='logout']
    account/ password_change/ [name='password_change']
    account/ password_change/done/ [name='password_change_done']
    account/ password_reset/ [name='password_reset']
    account/ password_reset/done/ [name='password_reset_done']
    account/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    account/ reset/done/ [name='password_reset_complete']
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
]
