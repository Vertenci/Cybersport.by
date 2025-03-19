from django.db import models
from teams.models import Teams
from tournaments.models import Tournaments
from matches.models import Matches


class Indicators(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, related_name='indicators_list', blank=True)
    tournament = models.ForeignKey(Tournaments, on_delete=models.SET_NULL, null=True, blank=True)
    match = models.ForeignKey(Matches, on_delete=models.SET_NULL, null=True, blank=True)

    wins = models.IntegerField('Количество побед', blank=True, null=True)
    loses = models.IntegerField('Количество поражений', blank=True, null=True)
    draws = models.IntegerField('Количество ничей', blank=True, null=True)
    achievements = models.TextField('Достижения', blank=True, null=True)

    def __str__(self):
        return str(self.team)

    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'
