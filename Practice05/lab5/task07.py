import re

s = input()
pattern = input()
replacement = input()

print(re.sub(re.escape(pattern), replacement, s))