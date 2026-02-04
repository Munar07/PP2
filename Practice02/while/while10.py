max_num = None  # пока нет чисел

while True:
    n = int(input())
    if n < 0:
        break
    if max_num is None or n > max_num:
        max_num = n

if max_num is None:
    print("Нет чисел")
else:
    print(max_num)
