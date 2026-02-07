from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

freq = Counter(arr)
max_freq = max(freq.values())
most_common = [k for k, v in freq.items() if v == max_freq]

print(min(most_common))
