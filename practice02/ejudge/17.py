from collections import Counter

n = int(input())
numbers = [input() for _ in range(n)]

freq = Counter(numbers)
count = sum(1 for v in freq.values() if v == 3)

print(count)
