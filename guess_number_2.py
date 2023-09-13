import random

print('игра началась')
print('угадай число от 1 до 20')

number = random.randint(1, 20)
win = False

for i in range(6):
    print('попытка номер', i)
    ans = int(input('введите число: '))
    if ans == number:
        win = True
        break
    elif ans < number:
        print('число больше')
    else:
        print('число меньше')

if win:
    print('вы выйграли')
else:
    print('вы проиграли')
    print('правильный ответ: ', number)