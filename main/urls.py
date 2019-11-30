from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('index', views.index),
    path('infinity', views.infinity),
    path('boy', views.boy),
    path('girl', views.girl),
    path('p1/<str:t>/', views.p11),
    path('p2', views.p22),
    path('p3', views.p33),
    path('p4', views.p44),
]
