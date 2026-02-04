import random
secret = random.randint(1, 10)

while True:
    guess = int(input("Введите число от 1 до 10: "))
    if guess == secret:
        print("Поздравляю! Вы угадали число.")
        break
    elif guess < secret:
        print("Слишком мало, попробуйте ещё.")
    else:
        print("Слишком много, попробуйте ещё.")
