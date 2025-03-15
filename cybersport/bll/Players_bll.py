from dal.repositories.PlayersRepository import PlayersRepository


class PlayersBLL:
    def __init__(self):
        self.players_dal = PlayersRepository()

    def fetch_all_players(self):
        return self.players_dal.get_all()

    def create_player(self, form):
        self.players_dal.insert(form.save())

    def delete_player(self, player_id):
        self.players_dal.delete(player_id)

    def get_player(self, player_id):
        return self.players_dal.get(player_id)

    def update_player(self, player):
        return self.players_dal.update(player)

    def fetch_players_by_game(self, game_id):
        return self.players_dal.get_players_by_game(game_id)
