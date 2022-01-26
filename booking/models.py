from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Pending"), (1, "Booked"))
TABLES = ((0, "Not assigned"), (1, "1"), (2, "2"), (3, "3"), (4, "4"),
          (5, "5"), (6, "6"), (7, "7"), (8, "8"), (9, "9"))
GUESTS = ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"),)
TYPE = ((0, "Lunch or Dinner>"), (1, "Lunch"), (2, "Dinner"),)


class Book(models.Model):
    used_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_books",
    )
    booked_time = models.TimeField()
    booked_date = models.DateField()
    menu_type = models.IntegerField(choices=TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    table_num = models.IntegerField(choices=TABLES, default=0)
    guests_num = models.IntegerField(choices=GUESTS)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.booked_date
