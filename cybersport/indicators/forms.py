from django.forms import ModelForm

from .models import Indicators


class IndicatorsForm(ModelForm):
    class Meta:
        model = Indicators
        fields = [
            'team',
            'tournament',
            'match',
            'wins',
            'loses',
            'draws',
            'achievements'
        ]
