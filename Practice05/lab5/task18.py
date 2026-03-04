import re

s = input()
pattern = input()

count = len(re.findall(re.escape(pattern), s))
print(count)