from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('', views.add_edit, name='add_edit'),
]