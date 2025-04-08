from django.db import models


class Games(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название игры', max_length=50, unique=True)
    icon = models.ImageField(upload_to='games/games_icon/', blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название игры'
        verbose_name_plural = 'Игры'
