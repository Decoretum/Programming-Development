# Generated by Django 4.2 on 2023-04-21 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
