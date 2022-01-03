# Generated by Django 4.0 on 2022-01-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0021_alter_menu_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='item_category',
            field=models.IntegerField(choices=[(0, 'Starter'), (1, 'Main Course'), (2, 'Dessert')]),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='menu_category',
            field=models.IntegerField(choices=[(1, 'Dinner'), (0, 'Lunch')], default=0),
        ),
    ]
