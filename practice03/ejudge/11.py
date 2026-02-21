# Класс Pair
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self, other):
        # Возвращаем новый объект Pair с суммой соответствующих значений
        return Pair(self.a + other.a, self.b + other.b)

# Чтение входных данных
a1, b1, a2, b2 = map(int, input().split())

# Создаём объекты Pair
p1 = Pair(a1, b1)
p2 = Pair(a2, b2)

# Складываем их
result = p1.add(p2)

# Выводим результат
print(f"Result: {result.a} {result.b}")
