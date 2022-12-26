class Room:
    def __init__(self, number: int, capacity: int):
        self.number: int = number
        self.capacity: int = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if not self.is_taken and people <= self.capacity:
            self.is_taken = True
            self.guests += people
            return
        return f"Room number {self.number} cannot be taken"

    def free_room(self):
        if self.is_taken:
            self.guests = 0
            self.is_taken = False
            return
        return f"Room number {self.number} is not taken"

