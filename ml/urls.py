"""ml URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .import views

urlpatterns = [
    path('form/',views.form,name='form'),
    path('admin/', admin.site.urls),
    path('results',views.result,name='result'),
    path('about/',views.about,name='about'),
    path('',views.home,name='home'),
    path('bmi/',views.bmi,name='bmi'),
    path('period_cal/',views.period_calculator,name='period_cal'),
    path('calory_cal/',views.cal_calculate,name='cal_calory'),
    path('widal/',views.widal,name='widal'),
    path('sugar/',views.sugar,name='sugar'),
    path('pregnancy_cal/',views.pregnancy_cal,name='pregnancy_cal'),
    path('anxiety/',views.anxiety_screening,name='anxiety'),
    path('medical/',views.medical,name='medical'),

]
