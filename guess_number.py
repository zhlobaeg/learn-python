import random

result = random.randrange(1, 10)
win = False

for i in range(1, 10):
    print('попытка номер: ', i)
    answer = int(input('Угадай число от 1 до 10: '))

    if answer == result:
        print('Угадал: ', result)
        win = True
        break
    elif answer > result:
        print('не угадал, число меньше')
    else:
        print('не угадал, число больше')

if win:
    print('Ты выиграл')
else:
    print('Ты проиграл')