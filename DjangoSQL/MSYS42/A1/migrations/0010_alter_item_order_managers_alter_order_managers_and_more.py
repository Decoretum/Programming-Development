# Generated by Django 4.2 on 2023-04-22 06:49

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0009_order_alter_item_description_item_order'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='item_order',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='order',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='amountpaid',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
