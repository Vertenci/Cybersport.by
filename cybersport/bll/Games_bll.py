from dal.repositories.GamesRepository import GamesRepository


class GamesBLL:
    def __init__(self):
        self.games_dal = GamesRepository()

    def fetch_all_games(self):
        return self.games_dal.get_all()

    def create_game(self, form):
        self.games_dal.insert(form.save())

    def delete_game(self, game_id):
        self.games_dal.delete(game_id)

    def get_game(self, game_id):
        return self.games_dal.get(game_id)

    def update_game(self, game):
        return self.games_dal.update(game)
