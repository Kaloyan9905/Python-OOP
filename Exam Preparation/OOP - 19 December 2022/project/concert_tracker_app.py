from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_TYPES = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }
    ROCK_SKILLS = [
        "play the drums with drumsticks",
        "sing high pitch notes",
        "play rock"
    ]
    METAL_SKILLS = [
        "play the drums with drumsticks",
        "sing low pitch notes",
        "play metal"
    ]
    JAZZ_SKILLS = [
        "play the drums with drum brushes",
        "sing low pitch notes",
        "sing high pitch notes",
        "play jazz"
    ]

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.MUSICIAN_TYPES:
            raise ValueError("Invalid musician type!")

        if any(m.name == name for m in self.musicians):
            raise Exception(f"{name} is already a musician!")

        musician = self.MUSICIAN_TYPES[musician_type](name, age)
        musician.skills = self.MUSICIAN_TYPES[musician_type].skills
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if any(b.name == name for b in self.bands):
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_concert_by_place(place)

        if concert:
            raise Exception(f"{concert.place} is already registered for {concert.genre} concert!")

        concert = Concert(
            genre,
            audience,
            ticket_price,
            expenses,
            place
        )
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)

        if musician is None:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.__find_band_by_name(band_name)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)

        if band is None:
            raise Exception(f"{band_name} isn't a band!")

        musician = self.__find_musician_who_is_in_band(musician_name, band)
        if musician is None:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        musician_types = {
            "Guitarist": 0,
            "Drummer": 0,
            "Singer": 0
        }
        band = self.__find_band_by_name(band_name)
        concert = self.__find_concert_by_place(concert_place)

        for member in band.members:
            musician_types[member.__class__.__name__] += 1

        if any(v == 0 for v in musician_types.values()):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == "Rock":
            allowed_skills = []
            for member in band.members:
                for skill in member.skills:
                    allowed_skills.append(skill)

            for skill in self.ROCK_SKILLS:
                if skill not in allowed_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Metal":
            allowed_skills = []
            for member in band.members:
                for skill in member.skills:
                    allowed_skills.append(skill)

            for skill in self.METAL_SKILLS:
                if skill not in allowed_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        if concert.genre == "Jazz":
            allowed_skills = []
            for member in band.members:
                for skill in member.skills:
                    allowed_skills.append(skill)

            for skill in self.JAZZ_SKILLS:
                if skill not in allowed_skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."

    def __find_musician_by_name(self, musician_name):
        for musician in self.musicians:
            if musician.name == musician_name:
                return musician
        return None

    def __find_band_by_name(self, band_name):
        for band in self.bands:
            if band.name == band_name:
                return band
        return None

    def __find_musician_who_is_in_band(self, musician_name, band):
        for musician in self.musicians:
            if musician.name == musician_name and musician in band.members:
                return musician
        return None

    def __find_concert_by_place(self, concert_place):
        for concert in self.concerts:
            if concert.place == concert_place:
                return concert
        return None
