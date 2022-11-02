class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours < 10:
            self.hours = f"0{self.hours}"

        if self.minutes < 10:
            self.minutes = f"0{self.minutes}"

        if self.seconds < 10:
            self.seconds = f"0{self.seconds}"

        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1

        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1

        if self.minutes > Time.max_minutes:
            self.minutes = 0
            self.hours += 1

        if self.hours > Time.max_hours:
            self.hours = 0

        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())


