from django.shortcuts import render
from .forms import MyCustomLoginForm, MySignupForm
from the_greenwich.forms import CustomSignupForm


def index(request):
    context = {
        'login_form': MyCustomLoginForm(), 
        'signup_form': CustomSignupForm()
    }
    # signupdisplay = CustomSignupForm
    return render(request, 'home/index.html',context)
