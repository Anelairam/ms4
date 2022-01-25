# Generated by Django 3.2 on 2022-01-25 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0014_alter_book_used_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='used_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_books', to=settings.AUTH_USER_MODEL),
        ),
    ]
