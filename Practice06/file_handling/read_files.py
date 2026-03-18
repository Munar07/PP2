with open("sample.txt", "r") as f:
    print(f.read())

with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)