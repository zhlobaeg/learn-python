import random

print('игра началась')
print('угадай число от 1 до 20 (3 режим)')
print('вы 2 раза вводите число которые складываются или вычитаются друг с другом(1 и 2 режимы)')
print('есть 3 режима 1 сложение, 2 вычитание, 3 обычный')
rezhim = int(input('1 режим, 2 или 3: '))
kolichestvo = int(input('1 (от 1 до 20) 2 (от 1 до 50) или 3 (от 1 до 100): '))

popitki = 0


if kolichestvo == 1:
    number = random.randint(1, 10)
    popitki = 6

elif kolichestvo == 2:
    number = random.randint(1, 50)
    popitki = 12

elif kolichestvo == 3:
    number = random.randint(1, 100)
    popitki = 15

def get_answer(rezhim):
    if rezhim == 1:
        ans = int(input('введите 1 число: '))
        print('                 +')
        ans_2 = int(input('введите 2 число: '))
        otvet = ans + ans_2
        return otvet
    elif rezhim == 2:
        ans = int(input('введите 1 число: '))
        print('                 -')
        ans_2 = int(input('введите 2 число: '))
        otvet = ans - ans_2
        return otvet
    elif rezhim == 3:
        ans = int(input('введите число: '))
        otvet = ans 
        return otvet  

def game(result, popitki, rezhim):
    for i in range(popitki):
        print('попытка номер', i, '/', popitki)

        otvet = get_answer(rezhim)

        if otvet == result:
            return True
        elif otvet < result:
            print('число больше')
        else:
            print('число меньше')

    return False

def game_result(win, number, rezhim):
    if win:
        print('вы выйграли')
        if rezhim != 3:
            print('правильный ответ: ', number)
    else:
        print('вы проиграли')
        print('правильный ответ: ', number)


if 1 <= rezhim <= 3:
    win = game(number, popitki, rezhim)
    game_result(win, number, rezhim)
else:
    print('bruh')