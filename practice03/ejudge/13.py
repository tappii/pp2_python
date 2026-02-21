import math

# Проверка, является ли число простым
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.isqrt(n)) + 1))

# Чтение входа
nums = list(map(int, input().split()))

# Фильтруем простые числа
primes = list(filter(is_prime, nums))

# Вывод результата
if primes:
    print(*primes)
else:
    print("No primes")
