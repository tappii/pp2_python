# Чтение входа
n = int(input())
arr = list(map(int, input().split()))
q = int(input())

# Чтение операций
operations = []
for _ in range(q):
    parts = input().split()
    op = parts[0]
    if op == "add":
        x = int(parts[1])
        operations.append(lambda a, x=x: a + x)
    elif op == "multiply":
        x = int(parts[1])
        operations.append(lambda a, x=x: a * x)
    elif op == "power":
        x = int(parts[1])
        operations.append(lambda a, x=x: a ** x)
    elif op == "abs":
        operations.append(lambda a: abs(a))

# Применяем операции последовательно
for f in operations:
    arr = list(map(f, arr))

# Вывод результата
print(*arr)
