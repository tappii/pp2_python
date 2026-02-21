import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# Чтение входного значения
r = int(input())

# Создание круга
c = Circle(r)

# Вывод площади с 2 знаками после запятой
print(f"{c.area():.2f}")
