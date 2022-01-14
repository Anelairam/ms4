from django.shortcuts import render
from . models import menu_item

# Create your views here.


def menu(request):
    starter = menu_item.objects.filter(item_category=0)
    mains = menu_item.objects.filter(item_category=1)
    deserts = menu_item.objects.filter(item_category=2)
    context = {
        'starters': starter,
        'mains': mains,
        'deserts': deserts,
    }
    return render(request, 'menu/menu.html', context)


def add_edit(request):
    return render(request, 'menu/add_edit.html')