def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        res = []
        for _ in range(n):
            res.append(next(seq))
        return res

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
