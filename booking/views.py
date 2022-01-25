from django.shortcuts import render
from .models import Book


# Renders the booking data into the booking template
def booking(request):
    booked = Book.objects.filter(status=1)
    pending = Book.objects.filter(status=0)
    context = {
        'booked': booked,
        'pending': pending

    }
    return render(request, 'booking/booking.html', context)
