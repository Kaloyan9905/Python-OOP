import itertools


def possible_permutations(lst):
    for perm in itertools.permutations(lst):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
