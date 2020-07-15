from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('upload/', views.upload, name='upload'),
    path('download/', views.download, name='download'),
    path('test/', views.test, name='test'),
]

