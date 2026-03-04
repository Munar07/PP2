import re

s = input()
sub = input()

print("Yes" if re.search(sub, s) else "No")