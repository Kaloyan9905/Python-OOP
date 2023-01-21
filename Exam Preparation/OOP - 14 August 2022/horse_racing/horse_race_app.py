from horse_racing.horse_race import HorseRace
from horse_racing.horse_specification.appaloosa import Appaloosa
from horse_racing.horse_specification.thoroughbred import Thoroughbred
from horse_racing.jockey import Jockey


class HorseRaceApp:
    VALID_TYPES_HORSES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_TYPES_HORSES:
            return None

        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")

        horse = self.VALID_TYPES_HORSES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.__find_horse_by_type(horse_type)
        if horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        jockey.horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)
        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda x: x.horse.speed, reverse=True)[0]
        return f"The winner of the {race_type} " \
               f"race, with a speed of {winner.horse.speed}km/h is " \
               f"{winner.name}! Winner's horse: {winner.horse.name}."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None

    def __find_horse_by_type(self, horse_type):
        self.horses.reverse()
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type and not horse.is_taken:
                self.horses.reverse()
                return horse
        return None

    def __find_race_by_type(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race
        return None
