# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # this is just an example
]
