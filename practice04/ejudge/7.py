class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # начинаем с конца строки

    def __iter__(self):
        return self  # объект сам является итератором

    def __next__(self):
        if self.index == 0:
            raise StopIteration  # сигнал, что элементы закончились
        self.index -= 1
        return self.data[self.index]


s = input()

for char in Reverse(s):
    print(char, end="")