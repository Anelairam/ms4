from django.shortcuts import render
from the_greenwich.forms import CustomSignupForm
from allauth.account.forms import LoginForm
# Create your views here.


def index(request):
    # signupdisplay = CustomSignupForm
    return render(request, 'home/index.html',)
