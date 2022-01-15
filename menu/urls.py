from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add/', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('delete/<item_id>', views.delete_item, name='delete'),
]