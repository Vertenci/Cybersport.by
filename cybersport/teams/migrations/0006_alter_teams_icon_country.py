# Generated by Django 5.1.5 on 2025-03-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_alter_teams_icon_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='icon_country',
            field=models.ImageField(blank=True, upload_to='teams/teams_images/country/'),
        ),
    ]
