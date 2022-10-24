n = int(input())

counter = 1

for i in range(n):
    print((" " * (n - counter)) + ' '.join("*" * counter))
    counter += 1

counter = n - 1
for i in range(n):
    print((" " * (n - counter)) + ' '.join("*" * counter))
    counter -= 1