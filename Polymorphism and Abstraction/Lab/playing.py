def start_playing(obj):
    return obj.play()


class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


class Children:
    @staticmethod
    def play():
        return "Playing the children"


children = Children()
print(start_playing(children))

guitar = Guitar()
print(start_playing(guitar))
