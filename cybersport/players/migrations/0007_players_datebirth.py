# Generated by Django 5.1.5 on 2025-03-04 20:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_players_draws_players_loses_players_wins'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='datebirth',
            field=models.DateTimeField(default=datetime.datetime(2000, 1, 1, 0, 0), verbose_name='Дата рождения'),
            preserve_default=False,
        ),
    ]
