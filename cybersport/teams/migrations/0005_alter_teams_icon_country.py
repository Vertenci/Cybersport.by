# Generated by Django 5.1.5 on 2025-03-05 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_teams_icon_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='icon_country',
            field=models.ImageField(blank=True, default='teams/teams_images/country/italy.png', upload_to='teams/teams_images/country/'),
        ),
    ]
