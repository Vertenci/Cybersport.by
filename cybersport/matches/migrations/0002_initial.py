# Generated by Django 5.1.5 on 2025-02-16 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
        ('teams', '0001_initial'),
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='team_one',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_team_match', to='teams.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='team_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_team_match', to='teams.teams'),
        ),
        migrations.AddField(
            model_name='matches',
            name='tournament',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.tournaments'),
        ),
    ]
