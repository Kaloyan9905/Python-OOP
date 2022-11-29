from players_and_monsters.elf import Elf


class MuseElf(Elf):
    def __init__(self, username: str, level: int):
        super().__init__(username, level)
