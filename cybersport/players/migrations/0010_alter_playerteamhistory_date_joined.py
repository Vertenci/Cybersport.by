# Generated by Django 5.1.5 on 2025-03-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0009_playerteamhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerteamhistory',
            name='date_joined',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата вступления'),
        ),
    ]
