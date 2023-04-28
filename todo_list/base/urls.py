from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('edit/<str:pk>/', views.updatePage, name='edit'),
    path('delete/<str:pk>/', views.deletePage, name='delete'),
]
