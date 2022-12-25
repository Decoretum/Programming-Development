# Generated by Django 4.0.2 on 2022-12-23 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, unique=True)),
                ('Brand', models.CharField(max_length=30)),
                ('Color', models.CharField(max_length=20)),
                ('Cost', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Userperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(max_length=50)),
            ],
        ),
    ]