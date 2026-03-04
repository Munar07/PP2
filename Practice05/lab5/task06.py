import re

s = input()

match = re.search(r"\S+@\S+\.\S+", s)

print(match.group() if match else "No email")