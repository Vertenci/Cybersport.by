# Generated by Django 5.1.5 on 2025-04-08 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_games_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='icon',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='games/games_icon/'),
        ),
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название игры'),
        ),
    ]
