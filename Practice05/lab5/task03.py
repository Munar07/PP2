import re

s = input()
pattern = input()

print(len(re.findall(re.escape(pattern), s)))