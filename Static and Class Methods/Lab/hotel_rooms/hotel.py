from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def status(self):
        total_guests = 0

        for room in self.rooms:
            total_guests += room.guests

        result = f"Hotel {self.name} has {total_guests} total guests\n"
        result += f"Free rooms: {', '.join([str(x.number) for x in self.rooms if not x.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}\n"

        return result
