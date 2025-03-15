from dal.repositories.MatchesRepository import MatchesRepository


class MatchesBLL:
    def __init__(self):
        self.matches_dal = MatchesRepository()

    def fetch_all_matches(self):
        return self.matches_dal.get_all()

    def create_match(self, form):
        self.matches_dal.insert(form.save())

    def delete_match(self, match_id):
        self.matches_dal.delete(match_id)

    def get_match(self, match_id):
        return self.matches_dal.get(match_id)

    def update_match(self, match):
        return self.matches_dal.update(match)

    def fetch_matches_by_game(self, game_id):
        return self.matches_dal.get_matches_by_game(game_id)