from django.forms import ModelForm

from .models import Matches


class MatchesForm(ModelForm):
    class Meta:
        model = Matches
        fields = [
            'game',
            'team_one',
            'team_two',
            'tournament',
            'date',
            'score'
        ]
