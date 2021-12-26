from django.shortcuts import render
from .models import Book


# Create your views here.

# Renders the booking data into the booking template
def booking(request):
    bookings = Book.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/booking.html', context)
    # return render(request, 'booking/booking.html') it works

