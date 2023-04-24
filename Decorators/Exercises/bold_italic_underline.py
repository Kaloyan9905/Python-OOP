def make_bold(func):
    def wrapper(*args):
        return "<b>" + func(*args) + "</b>"

    return wrapper


def make_italic(func):
    def wrapper(*args):
        return "<i>" + func(*args) + "</i>"

    return wrapper


def make_underline(func):
    def wrapper(*args):
        return "<u>" + func(*args) + "</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
