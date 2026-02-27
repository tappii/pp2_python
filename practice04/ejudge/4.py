def func(a,b):
    for i in range(a,b+1):
        yield i**2

a , b= list(map(int,input().split()))
for i in func(a,b):
    print(i)