# Generated by Django 5.0.6 on 2024-06-20 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0009_hotelbooking_rooms'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='rooms',
            new_name='room',
        ),
    ]