import random

player_num = int(input('загадай число от 1 до 10: '))
pc_num = random.randint(1, 10)

if player_num < 11 or player_num > 0:
    for i in range(10):          
            print('попытка ', i)
            if pc_num == player_num:
                print('ты проиграл')
                break
            else:
                print('ты победил', i + 1, 'раз.')
                break
else:
    print('я просил написать только числа от 1 до 10')
    print('>:(')
    print(' /')
    print('бан')