from    dal.repositories.TeamsRepository import TeamsRepository


class TeamsBLL:
    def __init__(self):
        self.teams_dal = TeamsRepository()

    def fetch_all_teams(self):
        return self.teams_dal.get_all()

    def create_team(self, form):
        self.teams_dal.insert(form.save())

    def delete_team(self, team_id):
        self.teams_dal.delete(team_id)

    def get_team(self, team_id):
        return self.teams_dal.get(team_id)

    def update_team(self, team):
        return self.teams_dal.update(team)

    def fetch_teams_by_game(self, game_id):
        return self.teams_dal.get_teams_by_game(game_id)
