from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('index', views.index),
    path('infinity', views.infinity),
    path('boy', views.boy),
    path('girl', views.girl),
]
