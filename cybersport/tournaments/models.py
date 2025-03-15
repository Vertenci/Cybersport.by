from django.db import models
from games.models import Games
from teams.models import Teams


class Tournaments(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Games, on_delete=models.SET_NULL, null=True)
    teams = models.ManyToManyField(Teams, blank=True)

    name = models.CharField('Название турнира', max_length=150)
    description = models.TextField('Описание')
    start_date = models.DateTimeField('Дата начала')
    end_date = models.DateTimeField('Дата окончания')
    sum_prize = models.IntegerField('Сумма призовых')
    location = models.CharField('Место проведения', max_length=150)

    def __str__(self):
        return (f"{self.name} | "
                f"Дата: {self.start_date} - {self.end_date}| "
                f"Призовой фонд: {self.sum_prize} | "
                f"Место: {self.location}")

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
