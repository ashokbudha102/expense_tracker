from django.shortcuts import render

# Create your views here.
from allauth.account.views import LoginView, SignupView


class MySignupView(SignupView):
    template_name='accounts/signup.html'

class MyLoginView(LoginView):
    template_name='accounts/login.html'