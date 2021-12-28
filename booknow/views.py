from django.shortcuts import render, redirect
from booking.models import Book
from booking.views import booking

# Create your views here.


def booknow(request):
    # if request.method == 'POST':
    #     # menu_type = request.POST.get('menu')
    #     date = request.POST.get('date')
    #     time = request.POST.get('time')
    #     guest_num = 'guest_num' in request.POST
    #     table_num = 'table_num' in request.POST
    #     print(date, time, guest_num, table_num)
    #     Book.objects.create(booked_time=time, booked_date=date, table_num=table_num, guests_num=guest_num)
    # #     return redirect('booking')

    return render(request, 'booknow/booknow.html')