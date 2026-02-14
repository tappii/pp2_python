n = int(input())
arr = [input() for _ in range(n)]
first_occurrence = {}

for i, s in enumerate(arr, 1):
    if s not in first_occurrence:
        first_occurrence[s] = i

for s in sorted(first_occurrence):
    print(s, first_occurrence[s])
