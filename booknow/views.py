from django.shortcuts import render

# Create your views here.


def booknow(request):
    return render(request, 'booknow/booknow.html')