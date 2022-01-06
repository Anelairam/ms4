from django import forms


TABLES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"))
GUESTS = ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"), )
TYPE = ((1, "Lunch"), (2, "Dinner"),)

class BookForm(forms.Form):
    menu = forms.ChoiceField(choices=TYPE)
    date = forms.DateField()
    time = forms.TimeField()
    guests = forms.ChoiceField(choices=GUESTS)
    tables = forms.ChoiceField(choices=TABLES)