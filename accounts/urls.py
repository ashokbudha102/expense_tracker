from django.urls import path
from .views import MyLoginView, MySignupView
urlpatterns = [
    path('login/',MyLoginView.as_view(), name='login'),
    path('accounts/signup/', MySignupView.as_view(), name='signup'),
]