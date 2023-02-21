def fibonacci():
    numbers = []
    index = 0

    while True:
        if len(numbers) == 0:
            numbers.append(0)
            yield 0

        elif len(numbers) == 1:
            numbers.append(1)
            yield 1

        elif len(numbers) >= 2:
            to_be_returned = numbers[index] + numbers[index + 1]
            numbers.append(to_be_returned)
            index += 1
            yield to_be_returned


generator = fibonacci()
for i in range(5):
    print(next(generator))
