from django.test import TestCase
from django.utils import timezone
from games.models import Games
from teams.models import Teams
from tournaments.models import Tournaments
from ..models import Matches


class MatchesModelTests(TestCase):
    def setUp(self):
        self.game = Games.objects.create(name="Game 1")
        self.team_one = Teams.objects.create(
            name="Team 1",
            founding_date=timezone.now(),
            prize=1000
        )
        self.team_two = Teams.objects.create(
            name="Team 2",
            founding_date=timezone.now(),
            prize=2000
        )
        self.tournament = Tournaments.objects.create(
            name="Tournament 1",
            description="Описание турнира",
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=1),
            sum_prize=5000,
            location="Location 1"
        )
        self.date = timezone.now()
        self.score = "1:0"
        self.match = Matches.objects.create(
            game=self.game,
            team_one=self.team_one,
            team_two=self.team_two,
            tournament=self.tournament,
            date=self.date,
            score=self.score
        )

    def test_matches_str(self):
        expected_str = (f"Матч: {self.team_one.name} vs {self.team_two.name} | "
                        f"Игра: {self.game.name} | "
                        f"Турнир: {self.tournament.name} | "
                        f"Дата: {self.date} | "
                        f"Счёт: {self.score} |")
        self.assertEqual(str(self.match), expected_str)
