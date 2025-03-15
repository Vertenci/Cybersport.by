# Generated by Django 5.1.5 on 2025-02-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_remove_tournaments_date_tournaments_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournaments',
            name='end_date',
            field=models.DateTimeField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='start_date',
            field=models.DateTimeField(verbose_name='Дата начала'),
        ),
    ]
