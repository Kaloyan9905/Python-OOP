def squares(n):
    counter = 1

    while counter <= n:
        yield counter ** 2
        counter += 1


print(list(squares(5)))
