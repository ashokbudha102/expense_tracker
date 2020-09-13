from django.contrib import admin
from django.urls import path
from .views import home_view, homeCreateView,expenseDeleteView, downloadView
urlpatterns = [
    path('',home_view, name='home'),
    path('create/', homeCreateView.as_view(), name='create-home'),
    path('<int:pk>/delete/', expenseDeleteView.as_view(), name='expense_delete'),
    path('download/',downloadView, name='download'),

]
