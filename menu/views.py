from django.shortcuts import render
from . models import menu_item

# Create your views here.


def menu(request):
    menus = menu_item.objects.all()
    context = {
        'menus': menus
    }
    return render(request, 'menu/menu.html', context)
