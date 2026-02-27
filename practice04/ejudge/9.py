def powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i


n = int(input())

for p in powers_of_two(n):
    print(p, end=" ")