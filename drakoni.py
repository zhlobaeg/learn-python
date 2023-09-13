import random

print('игра началась')

game_on = True

while game_on:

    number = random.randint(1, 2)
    print('выбери пещеру что-бы выжить')
    ans = int(input('1 или 2: '))
    
    if ans == number:
        print('вы выйграли')
        game_on = False
    else:
        print('вы проиграли')
        rip = input('хотите попробовать ещё раз?')
        if rip == 'нет':
            game_on = False