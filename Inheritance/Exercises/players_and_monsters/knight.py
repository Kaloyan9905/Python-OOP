from players_and_monsters.hero import Hero


class Knight(Hero):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)