from django.shortcuts import render, redirect
from .models import Book, TestForms


# Create your views here.

# Renders the booking data into the booking template
def booking(request):
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_date = request.POST.get('date')
        new_time = request.POST.get('time')
        TestForms.objects.create(title=new_title, date=new_date, time=new_time)
        return redirect('booking')
    else:
        print(request.GET)
    bookings = Book.objects.all()
    tests = TestForms.objects.all()
    context = {
        'bookings': bookings,
        'tests': tests
    }
    return render(request, 'booking/booking.html', context)
    # return render(request, 'booking/booking.html') it works
