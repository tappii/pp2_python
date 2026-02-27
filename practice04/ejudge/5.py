def func(a):
    while a >= 0:
        yield a
        a-=1

x = int(input())
for i in func(x):
    print(i)