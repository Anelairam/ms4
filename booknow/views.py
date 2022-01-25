from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookForm

# Create your views here.


def booknow(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.used_id = request.user
            instance.save()
            messages.success(request, 'You have requested a booking we will'
                                      'confirm it as soon as possible')
            return redirect('../booking')

    form = BookForm()

    return render(request, 'booknow/booknow.html', {'form': form})
