from django.shortcuts import render
from .models import menu_item
from .form import addItemForm

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
    if request.method == "POST":
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
   
    form = addItemForm()

    return render(request, 'menu/add_edit.html', {'form': form})
