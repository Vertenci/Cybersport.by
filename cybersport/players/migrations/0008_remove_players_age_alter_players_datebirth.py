# Generated by Django 5.1.5 on 2025-03-04 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_players_datebirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='age',
        ),
        migrations.AlterField(
            model_name='players',
            name='datebirth',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
