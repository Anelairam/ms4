from django import forms
from . models import menu_item


class addItemForm(forms.ModelForm):

    class Meta:
        model = menu_item
        fields = '__all__'