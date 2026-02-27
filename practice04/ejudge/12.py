import json

def find_diffs(obj1, obj2, path=""):
    diffs = []
    keys = set(obj1.keys()) | set(obj2.keys())
    
    for key in keys:
        new_path = f"{path}.{key}" if path else key
        in1 = key in obj1
        in2 = key in obj2
        
        val1 = obj1.get(key, "<missing>")
        val2 = obj2.get(key, "<missing>")
        
        if in1 and in2:
            # both exist
            if isinstance(val1, dict) and isinstance(val2, dict):
                diffs.extend(find_diffs(val1, val2, new_path))
            elif val1 != val2:
                diffs.append((new_path, val1, val2))
        else:
            diffs.append((new_path, val1, val2))
    return diffs

# read input
obj1 = json.loads(input().strip())
obj2 = json.loads(input().strip())

# find differences
diffs = find_diffs(obj1, obj2)

if not diffs:
    print("No differences")
else:
    for path, old, new in sorted(diffs):
        old_json = json.dumps(old, separators=(',', ':')) if old != "<missing>" else "<missing>"
        new_json = json.dumps(new, separators=(',', ':')) if new != "<missing>" else "<missing>"
        print(f"{path} : {old_json} -> {new_json}")