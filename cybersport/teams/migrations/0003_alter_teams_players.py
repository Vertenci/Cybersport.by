# Generated by Django 5.1.5 on 2025-02-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_alter_players_team'),
        ('teams', '0002_remove_teams_player_teams_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='teams', to='players.players'),
        ),
    ]
