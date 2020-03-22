 # this is my urls.py file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about.html', views.about, name = "about"),
    path('catalog.html', views.catalog, name = "catalog"),
    path('activate.html', views.activate, name = "activate"),
    path('logs.html', views.logs, name = "logs"),

]
