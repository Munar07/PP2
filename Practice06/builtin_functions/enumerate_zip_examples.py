names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

nums = [5, 2, 9, 1]
print(sorted(nums))

x = "123"
print(int(x), float(x))