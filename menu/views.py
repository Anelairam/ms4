from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
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


def add_item(request):
    if request.method == "POST":
        form = addItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added a new dish'
                                      'in the menu')
            return redirect('menu')
    form = addItemForm()
    context = {
        'form': form
    }
    return render(request, 'menu/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(menu_item, id=item_id)
    if request.method == "POST":
        form = addItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully edited a dish '
                                      'from the menu')
            return redirect('menu')
    form = addItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'menu/edit_item.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(menu_item, id=item_id)
    item.delete()
    messages.success(request, 'You have successfully deleted a dish from '
                              'the menu')
    return render(request, 'menu/menu.html')
