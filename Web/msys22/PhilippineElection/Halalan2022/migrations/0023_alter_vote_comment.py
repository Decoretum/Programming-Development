# Generated by Django 4.0.2 on 2022-05-17 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Halalan2022', '0022_alter_vote_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='comment',
            field=models.CharField(default='Add Comments', max_length=1000),
        ),
    ]
