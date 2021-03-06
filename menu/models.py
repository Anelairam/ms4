from django.db import models


ITEM_TYPE = {(0, "Starter"), (1, "Main Course"), (2, "Dessert")}


class menu_item(models.Model):
    title = models.CharField(max_length=200, unique=True)
    components = models.TextField(max_length=5000)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    created_on = models.DateField(auto_now_add=True)
    item_category = models.IntegerField(choices=ITEM_TYPE)


    def __str__(self):
        return self.title
