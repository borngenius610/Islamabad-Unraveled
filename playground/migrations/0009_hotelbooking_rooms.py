# Generated by Django 5.0.6 on 2024-06-20 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0008_hotelbooking_srno'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelbooking',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
    ]