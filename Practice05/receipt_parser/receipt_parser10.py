import re

s = input()
snake_case = re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_")
print(snake_case)