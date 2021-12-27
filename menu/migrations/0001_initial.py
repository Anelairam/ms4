# Generated by Django 4.0 on 2021-12-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('components', models.CharField(max_length=5000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('meny_category', models.IntegerField(choices=[(0, 'Lunch'), (1, 'Dinner')])),
                ('item_category', models.IntegerField(choices=[(0, 'Dessert'), (0, 'Main Course'), (0, 'Starter')])),
            ],
        ),
    ]
