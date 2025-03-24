from django.shortcuts import render
from bll.Tournaments_bll import TournamentsBLL
from django.views.generic import DetailView

from .models import Tournaments


def tour_home(request):
    tour_bll = TournamentsBLL()
    tournaments = tour_bll.fetch_all_tournaments()
    return render(request, 'tournaments/main_tour.html', {'tournaments': tournaments})


class TournamentsDetailView(DetailView):
    model = Tournaments
    template_name = 'tournaments/detail_tournaments.html'
    context_object_name = 'tournament'

    def get_object(self, queryset=None):
        bll = TournamentsBLL()
        return bll.get_tournament(self.kwargs['pk'])
