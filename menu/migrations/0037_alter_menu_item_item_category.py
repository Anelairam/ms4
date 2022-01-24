# Generated by Django 4.0 on 2022-01-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0036_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(2, 'Dessert'), (1, 'Main Course'), (0, 'Starter')]),
        ),
    ]
