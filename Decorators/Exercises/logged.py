def logged(function):
    def decorator(*args):
        values = [arg for arg in args]
        return f"you called {function.__name__}({', '.join([str(v) for v in values])})\n" + \
               f"it returned {function(*args)}"

    return decorator


@logged
def func(*args):
    return 3 + len(args)


result = func(4, 4, 4)
print(result)
