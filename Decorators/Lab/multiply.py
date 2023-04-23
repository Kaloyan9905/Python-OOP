def multiply(times):
    def decorator(function):
        def wrapper(num):
            res = function(num)
            return res * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
