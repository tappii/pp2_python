# Базовый класс Employee
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def total_salary(self):
        return self.base_salary

# Класс Manager — добавляет процент бонуса
class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent
    
    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

# Класс Developer — добавляет премию за проекты
class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects
    
    def total_salary(self):
        return self.base_salary + 500 * self.completed_projects

# Класс Intern — без бонусов
class Intern(Employee):
    pass  # использует метод базового класса

# Чтение входных данных
data = input().split()
role = data[0]
name = data[1]
base_salary = int(data[2])

# Создание объекта в зависимости от роли
if role == "Manager":
    bonus_percent = int(data[3])
    emp = Manager(name, base_salary, bonus_percent)
elif role == "Developer":
    completed_projects = int(data[3])
    emp = Developer(name, base_salary, completed_projects)
else:
    emp = Intern(name, base_salary)

# Вывод информации с 2 знаками после запятой
print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")
