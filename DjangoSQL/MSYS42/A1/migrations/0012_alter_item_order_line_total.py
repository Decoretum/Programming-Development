# Generated by Django 4.2 on 2023-04-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0011_rename_stock_item_stock_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_order',
            name='line_total',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
