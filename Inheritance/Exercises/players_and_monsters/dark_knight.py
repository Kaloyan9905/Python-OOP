from players_and_monsters.knight import Knight


class DarkKnight(Knight):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)