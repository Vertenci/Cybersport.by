# Generated by Django 5.1.5 on 2025-02-19 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0003_initial'),
        ('matches', '0002_initial'),
        ('teams', '0001_initial'),
        ('tournaments', '0003_alter_tournaments_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicators',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='matches.matches'),
        ),
        migrations.AlterField(
            model_name='indicators',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='indicators_list', to='teams.teams'),
        ),
        migrations.AlterField(
            model_name='indicators',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tournaments.tournaments'),
        ),
    ]
