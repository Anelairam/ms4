from django.shortcuts import render

# Create your views here.
def new_booking(request):
    return render(request, 'new_booking/new_booking.html')
