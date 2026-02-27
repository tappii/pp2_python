import json
import re

def resolve_query(data, query):
    tokens = re.findall(r'\w+|\[\d+\]', query)
    current = data
    for token in tokens:
        if token.startswith('['):
            index = int(token[1:-1])
            if isinstance(current, list) and 0 <= index < len(current):
                current = current[index]
            else:
                return "NOT_FOUND"
        else:
            if isinstance(current, dict) and token in current:
                current = current[token]
            else:
                return "NOT_FOUND"
    return json.dumps(current, separators=(',', ':'))

data = json.loads(input().strip())
n = int(input())
for _ in range(n):
    query = input().strip()
    print(resolve_query(data, query))