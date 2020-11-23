from django.contrib import admin
from django.urls import path
from .views import home_view,delete_item,summary
urlpatterns = [
    path('',home_view, name='home'),
    path('delete/<int:pk>',delete_item, name='delete'),
    path('summary',summary, name='summary'),
]
