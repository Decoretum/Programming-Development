# Generated by Django 4.2 on 2023-04-21 14:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('A1', '0007_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=200)),
                ('stock', models.IntegerField(default=0)),
                ('outofstock', models.BooleanField(default=False)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]