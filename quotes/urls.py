"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""

from . import views
from django.urls import path , include
# from django.conf.urls import url
from django.urls import re_path as url
urlpatterns = [
    path('',views.home, name='home'),
    path('about.html',views.about, name='about'),
    path('base.html',views.base, name='base'),
    path('add_stock.html',views.add_stock , name='add_stock'),
]