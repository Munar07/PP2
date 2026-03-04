import re

s = input()
pattern = re.compile(r"^\d+$")

print("Match" if pattern.fullmatch(s) else "No match")