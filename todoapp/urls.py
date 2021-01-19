from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    
    path('',views.home, name= 'home'),
    path('update_taask/<str:pk>',views.UpdateTask, name= 'update_task'),
    path('delete/<str:pk>',views.deletetask, name= 'delete'),
]