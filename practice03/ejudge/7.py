import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# Чтение координат
x1, y1 = map(int, input().split())  # начальная точка
x2, y2 = map(int, input().split())  # новые координаты
x3, y3 = map(int, input().split())  # вторая точка для расстояния

# Создаем начальную точку
p1 = Point(x1, y1)
p1.show()

# Перемещаем точку
p1.move(x2, y2)
p1.show()

# Создаем вторую точку
p2 = Point(x3, y3)

# Считаем расстояние и выводим с 2 знаками после запятой
print(f"{p1.dist(p2):.2f}")
