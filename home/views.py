from django.shortcuts import render
from .forms import MyCustomLoginForm


def index(request):
    context = {
        'login_form': MyCustomLoginForm(),
    }
    return render(request, 'home/index.html', context)
