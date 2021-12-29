from django.shortcuts import render
from .forms import MyCustomLoginForm, MySignupForm


def index(request):
    context = {
        'login_form': MyCustomLoginForm(), 
        'signup_form': MySignupForm()
    }
    # signupdisplay = CustomSignupForm
    return render(request, 'home/index.html',context)
