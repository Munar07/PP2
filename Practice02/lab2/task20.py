n = int(input())
doc = {}
for _ in range(n):
    line = input().strip()
    if line.startswith("set"):
        _, key, value = line.split()
        doc[key] = value
    elif line.startswith("get"):
        _, key = line.split()
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")