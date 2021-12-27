from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
MENU_TYPE = {(0, "Lunch"), (1, "Dinner")}
ITEM_TYPE = {(0, "Starter"), (0, "Main Course"), (0, "Dessert")}


class menu_item(models.Model):
    title = models.CharField(max_length=200, unique=True)
    components = models.CharField(max_length=5000)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # employee_id = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)
    meny_category = models.IntegerField(choices=MENU_TYPE)
    item_category = models.IntegerField(choices=ITEM_TYPE)

