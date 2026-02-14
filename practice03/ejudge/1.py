x = int(input())
valid = False
while x > 0:
    if(x%10)%2==0:
        valid = True
        break
    x//=10

if (valid):
        print("Valid")
else:
        print("Not valid")