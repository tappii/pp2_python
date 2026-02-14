digits = {
    "ZER": "0","ONE": "1","TWO": "2","THR": "3","FOU": "4",
    "FIV": "5","SIX": "6","SEV": "7","EIG": "8","NIN": "9"
}

a = input()
b = input()
op = input()


for key in digits:
    a = a.replace(key, digits[key])
    b = b.replace(key, digits[key])


result = str(eval(a + op + b))


reverse = {v:k for k,v in digits.items()}


answer = ""
for digit in result:
    answer += reverse[digit]

print(answer)