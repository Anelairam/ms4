# Generated by Django 3.2 on 2022-01-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0042_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(2, 'Dessert'), (0, 'Starter'), (1, 'Main Course')]),
        ),
    ]
