from football_team_generator.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for player_info in self.__players:
            if player_info.name == player.name:
                return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for player_info in self.__players:
            if player_info.name == player_name:
                self.__players.remove(player_info)
                return player_info

        return f"Player {player_name} not found"



