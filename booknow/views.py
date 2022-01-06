from django.shortcuts import render, redirect
from .forms import BookForm

# Create your views here.


def booknow(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = BookForm()

    return render(request, 'booknow/booknow.html', {'form': form})
