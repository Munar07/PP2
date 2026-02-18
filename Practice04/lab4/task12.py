import json

a = json.loads(input())
b = json.loads(input())

diffs = []

def find_diffs(x, y, path=""):
    keys = set(x.keys()) | set(y.keys())
    for k in sorted(keys):
        new_path = f"{path}.{k}" if path else k
        xv = x.get(k, "<missing>")
        yv = y.get(k, "<missing>")
        # Use literal <missing> if key absent
        xv_str = json.dumps(xv, separators=(',', ':')) if xv != "<missing>" else "<missing>"
        yv_str = json.dumps(yv, separators=(',', ':')) if yv != "<missing>" else "<missing>"
        if isinstance(xv, dict) and isinstance(yv, dict):
            find_diffs(xv, yv, new_path)
        elif xv_str != yv_str:
            diffs.append(f"{new_path} : {xv_str} -> {yv_str}")

find_diffs(a, b)

if diffs:
    for line in diffs:
        print(line)
else:
    print("No differences")
