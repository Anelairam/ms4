from django.shortcuts import render
from .forms import MyCustomLoginForm


def index(request):
    context = {
        'login_form': MyCustomLoginForm(), 
        # 'signup_form': SignupForm()
    }
    # signupdisplay = CustomSignupForm
    return render(request, 'home/index.html',context)
