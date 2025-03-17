from django.db import models
from games.models import Games


class Teams(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)
    players = models.ManyToManyField('players.Players', related_name='teams', blank=True)
    indicators = models.ForeignKey('indicators.Indicators', on_delete=models.SET_NULL, null=True, related_name='teams')

    name = models.CharField('Название команды', max_length=100)
    icon = models.ImageField(upload_to='teams/teams_images/', null=True, blank=True)
    founding_date = models.DateTimeField('Дата основания')
    team_history = models.TextField('История команды')
    prize = models.IntegerField('Призовые')
    country = models.CharField('Страна', max_length=100)
    icon_country = models.ImageField(upload_to='teams/teams_images/country/', blank=True, null=True)
    site = models.CharField('Сайт', max_length=100, default='site.ru')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название команды'
        verbose_name_plural = 'Названия команд'
