from django.db import models
from games.models import Games
from teams.models import Teams
from tournaments.models import Tournaments


class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)
    team_one = models.ForeignKey(Teams, related_name='first_team_match', on_delete=models.SET_NULL, null=True)
    team_two = models.ForeignKey(Teams, related_name='second_team_match', on_delete=models.SET_NULL, null=True)
    tournament = models.ForeignKey(Tournaments, on_delete=models.SET_NULL, null=True)

    date = models.DateTimeField('Дата матча')
    score = models.CharField('Счёт', max_length=35)

    def __str__(self):
        return (f"Матч: {self.team_one.name} vs {self.team_two.name} | "
                f"Игра: {self.game.name} | "
                f"Турнир: {self.tournament.name} | "
                f"Дата: {self.date} | "
                f"Счёт: {self.score} |")

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
