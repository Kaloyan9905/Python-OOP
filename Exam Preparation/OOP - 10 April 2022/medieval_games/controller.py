from medieval_games.player import Player
from medieval_games.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_TYPES = ["Food", "Drink"]
    STAMINA = 0
    STAMINA_1 = 0
    STAMINA_2 = 0

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        current_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                current_added_players.append(player)

        return f"Successfully added: {', '.join([p.name for p in current_added_players])}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)

        if player is None or sustenance_type not in self.VALID_SUSTENANCE_TYPES:
            return None

        supply, index = self.__find_supply_by_sustenance_type(sustenance_type)
        if supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.stamina == 100:
            return f"{player_name} have enough stamina."

        self.STAMINA = player.stamina
        self.STAMINA += supply.energy
        if self.STAMINA > 100:
            self.STAMINA = 100
        player.stamina = self.STAMINA

        self.supplies.pop(index)
        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_1 = self.__find_player_by_name(first_player_name)
        player_2 = self.__find_player_by_name(second_player_name)

        if player_1.stamina == 0 and player_2.stamina == 0:
            result = f"Player {first_player_name} does not have enough stamina.\n"
            result += f"Player {second_player_name} does not have enough stamina."
            return result

        if player_1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."

        if player_2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        self.STAMINA_1 = player_1.stamina
        self.STAMINA_2 = player_2.stamina

        if self.__returns_energy_with_bool(player_1, player_2):
            self.STAMINA_2 = self.__first_player_attacks(player_1)
            if self.STAMINA_2 <= 0:
                player_2.stamina = 0
                return f"Winner: {player_1.name}"
            player_2.stamina = self.STAMINA_2

            self.STAMINA_1 = self.__second_player_attacks(player_2)
            if self.STAMINA_1 <= 0:
                player_1.stamina = 0
                return f"Winner: {player_2.name}"
            player_1.stamina = self.STAMINA_1

        else:
            self.STAMINA_1 = self.__second_player_attacks(player_2)
            if self.STAMINA_1 <= 0:
                player_1.stamina = 0
                return f"Winner: {player_2.name}"
            player_1.stamina = self.STAMINA_1

            self.STAMINA_2 = self.__first_player_attacks(player_1)
            if self.STAMINA_2 <= 0:
                player_2.stamina = 0
                return f"Winner: {player_1.name}"
            player_2.stamina = self.STAMINA_2

        if self.__returns_energy_with_bool(player_1, player_2):
            return f"Winner: {player_2.name}"
        return f"Winner: {player_1.name}"

    def next_day(self):
        for player in self.players:
            self.STAMINA = player.stamina
            self.STAMINA -= player.age * 2
            if self.STAMINA <= 0:
                self.STAMINA = 0
            player.stamina = self.STAMINA

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = ""
        for player in self.players:
            result += f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}\n"

        result.strip()

        for supply in self.supplies:
            result += f"{supply.__class__.__name__}: {supply.name}, {supply.energy}\n"

        return result.strip()

    def __find_player_by_name(self, player_name):
        # player = [p for p in self.players if p.name == player_name][0]
        # return player
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def __find_supply_by_sustenance_type(self, sustenance_type):
        for index in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[index].__class__.__name__ == sustenance_type:
                return self.supplies[index], index
        return None, None

    @staticmethod
    def __returns_energy_with_bool(player_1, player_2):
        return player_1.stamina < player_2.stamina

    def __first_player_attacks(self, player_1):
        self.STAMINA_2 -= player_1.stamina / 2
        return self.STAMINA_2

    def __second_player_attacks(self, player_2):
        self.STAMINA_1 -= player_2.stamina / 2
        return self.STAMINA_1
