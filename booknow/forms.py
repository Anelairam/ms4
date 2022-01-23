from django import forms
from booking.models import Book



class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'booked_time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'booked_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'type':'date'}),
        }

