from datetime import date
from django.db import models
from games.models import Games


class Players(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey('teams.Teams', on_delete=models.SET_NULL, null=True, blank=True, related_name='players_in_team')
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True, blank=True)

    nickname = models.CharField('Ник', max_length=100, unique=True)
    fio = models.CharField('ФИО', max_length=250, unique=True)
    datebirth = models.DateField('Дата рождения')
    country = models.CharField('Страна', max_length=100)
    icon_country = models.ImageField(upload_to='players/players_images/country/')
    photo = models.ImageField(upload_to='players/players_images/')
    sum_prize = models.IntegerField('Сумма призовых', null=False, blank=True, default=0)
    description = models.TextField('Описание', blank=True)
    wins = models.IntegerField('Количество побед', blank=True, null=False, default=0)
    draws = models.IntegerField('Количество ничей', blank=True, null=False, default=0)
    loses = models.IntegerField('Количество поражений', blank=True, null=False, default=0)

    def __str__(self):
        return self.nickname

    @property
    def age(self):
        today = date.today()
        age = today.year - self.datebirth.year - ((today.month, today.day) < (self.datebirth.month, self.datebirth.day))
        return age

    class Meta:
        verbose_name = 'Игрок'
        verbose_name_plural = 'Игроки'


class PlayerTeamHistory(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE, related_name='team_history')
    team = models.ForeignKey('teams.Teams', on_delete=models.CASCADE)
    date_joined = models.DateTimeField('Дата вступления', null=True, blank=True)
    date_left = models.DateTimeField('Дата выхода', null=True, blank=True)

    def __str__(self):
        return f"{self.player.nickname} в {self.team.name}"

    class Meta:
        unique_together = ('player', 'team')
