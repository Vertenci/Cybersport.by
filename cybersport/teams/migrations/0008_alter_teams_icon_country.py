# Generated by Django 5.1.5 on 2025-03-17 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_teams_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='icon_country',
            field=models.ImageField(blank=True, null=True, upload_to='teams/teams_images/country/'),
        ),
    ]
