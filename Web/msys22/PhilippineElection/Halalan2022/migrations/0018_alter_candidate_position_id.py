# Generated by Django 4.0.2 on 2022-05-15 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Halalan2022', '0017_userperson_alter_vote_user_id_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='position_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Halalan2022.position'),
        ),
    ]
