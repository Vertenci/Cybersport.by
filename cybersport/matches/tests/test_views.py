from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from games.models import Games
from teams.models import Teams
from tournaments.models import Tournaments
from ..models import Matches


class MatchViewTests(TestCase):
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

    def test_match_home_view(self):
        response = self.client.get('/matches/home-matches/')
        self.assertRedirects(response, '/matches/home-matches/', status_code=301, target_status_code=200)
        self.assertIn('matches', response.context)
        self.assertEqual(len(response.context['matches']), 1)
        self.assertEqual(response.context['matches'][0].id, self.match.id)

    def test_match_detail_view(self):
        response = self.client.get(reverse('match_detail', args=[self.match.id]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['match'].id, self.match.id)
