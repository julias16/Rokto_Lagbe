"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('bloodreq/', views.bloodreq, name='bloodreq'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login, name='login'),
    path('searchdonors/', views.searchdonors, name='searchdonors'),
    path('signup/', views.signup, name='signup'),
    path('different_blood_groups/', views.different_blood_groups, name='different_blood_groups'),
    path('different_blood_terms/', views.different_blood_terms, name='different_blood_terms'),
    path('how_often_can_i_donate_blood/', views.how_often_can_i_donate_blood, name='how_often_can_i_donate_blood'),
    path('what_is_blood/', views.what_is_blood, name='what_is_blood'),
    path('what_is_blood_donation/', views.what_is_blood_donation, name='what_is_blood_donation'),
    path('who_can_donate_blood/', views.who_can_donate_blood, name='who_can_donate_blood'),






    path(' ', include('users.urls')),
]
