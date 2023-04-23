def vowel_filter(function):
    vowels = ["a", "e", "i", "u", "o"]

    def wrapper():
        return [v for v in function() if v in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
