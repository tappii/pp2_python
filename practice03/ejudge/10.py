# Базовый класс
class Person:
    def __init__(self, name):
        self.name = name

# Класс-наследник
class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)  # вызываем конструктор родителя
        self.gpa = gpa
    
    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

# Чтение входа
data = input().split()
name = data[0]
gpa = float(data[1])

# Создаём студента и выводим информацию
s = Student(name, gpa)
s.display()
