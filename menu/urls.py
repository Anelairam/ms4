from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add_edit/', views.add_edit, name='add_edit'),
]