from django.forms import ModelForm

from .models import Tournaments


class TournamentsForm(ModelForm):
    class Meta:
        model = Tournaments
        fields = [
            'name',
            'description',
            'start_date',
            'end_date',
            'sum_prize',
            'location',
            'game',
            'teams'
        ]