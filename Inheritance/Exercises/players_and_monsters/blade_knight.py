from players_and_monsters.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)