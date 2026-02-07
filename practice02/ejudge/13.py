x = int(input())
if x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1)):
    print("Yes")
else:
    print("No")
