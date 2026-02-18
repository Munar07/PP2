import json
import re

data = json.loads(input())
q = int(input())
queries = [input() for _ in range(q)]

for query in queries:
    current = data
    found = True
    # Split by dots
    parts = query.split(".")
    try:
        for part in parts:
            # Match key followed by optional brackets, e.g., friends[2][0]
            while part:
                m = re.match(r'^([^\[\]]+)', part)
                if m:
                    key = m.group(1)
                    current = current[key]
                    part = part[m.end():]
                else:
                    m = re.match(r'^\[(\d+)\]', part)
                    if m:
                        idx = int(m.group(1))
                        current = current[idx]
                        part = part[m.end():]
                    else:
                        raise KeyError
    except (KeyError, IndexError, TypeError):
        found = False

    if found:
        print(json.dumps(current, separators=(',', ':')))
    else:
        print("NOT_FOUND")
