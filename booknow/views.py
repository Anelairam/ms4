from django.shortcuts import render, redirect
# from booking.models import Book
# from booking.views import booking
from .forms import BookForm

# Create your views here.


def booknow(request):
    if request.method == "post":
        form = BookForm(request.POST)
        if form.is_valid():
            print('VALID')

    form = BookForm()

    return render(request, 'booknow/booknow.html', {'form': form})