class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
counter = Counter()
counter.increment()
print(counter.count)