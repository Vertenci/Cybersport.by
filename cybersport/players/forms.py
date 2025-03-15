from django.forms import ModelForm
from .models import Players, PlayerTeamHistory


class PlayersForm(ModelForm):
    class Meta:
        model = Players
        fields = [
            'nickname',
            'fio',
            'datebirth',
            'country',
            'icon_country',
            'photo',
            'sum_prize',
            'description',
            'wins',
            'draws',
            'loses',
            'team',
            'game',
            'age'
        ]


class PlayerTeamHistoryForm(ModelForm):
    class Meta:
        model = PlayerTeamHistory
        fields = [
            'player',
            'team',
            'date_joined',
            'date_lef'
        ]
