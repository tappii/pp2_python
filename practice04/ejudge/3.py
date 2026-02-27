x = int(input().strip())
for i in range(0, x+1,12):
    if i != 0:
        print(" ", end="")
    print(i, end="")