# Generated by Django 5.1.5 on 2025-03-12 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0005_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
