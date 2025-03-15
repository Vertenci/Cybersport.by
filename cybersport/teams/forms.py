from django.forms import ModelForm
from .models import Teams


class TeamsForm(ModelForm):
    class Meta:
        model = Teams
        fields = [
            'name',
            'icon',
            'founding_date',
            'team_history',
            'prize',
            'country',
            'icon_country',
            'game',
            'players',
            'indicators',
            'site'
        ]
