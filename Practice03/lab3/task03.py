digit_map = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"
}
reverse_map = {v: k for k, v in digit_map.items()}
s = input()
for op in ['+', '-', '*']:
    if op in s:
        left, right = s.split(op)
        operator = op
        break
def convert_to_number(text):
    num = ""
    for i in range(0, len(text), 3):
        num += digit_map[text[i:i+3]]
    return int(num)
a = convert_to_number(left)
b = convert_to_number(right)
if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
else:
    result = a * b
result_str = str(result)
output = ""
for digit in result_str:
    output += reverse_map[digit]
print(output)