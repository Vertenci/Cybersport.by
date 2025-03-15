from dal.repositories.TournamentsRepository import TournamentsRepository


class TournamentsBLL:
    def __init__(self):
        self.tournaments_dal = TournamentsRepository()

    def fetch_all_tournaments(self):
        return self.tournaments_dal.get_all()

    def create_tournament(self, form):
        self.tournaments_dal.insert(form.save())

    def delete_tournament(self, tournament_id):
        self.tournaments_dal.delete(tournament_id)

    def get_tournament(self, tournament_id):
        return self.tournaments_dal.get(tournament_id)

    def update_tournament(self, tournament):
        return self.tournaments_dal.update(tournament)
