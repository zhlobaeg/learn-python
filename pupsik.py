import random

print('игра началась')
print('угадай число от 1 до 20 (3 режим)')
print('вы 2 раза вводите число которые складываются или вычитаются друг с другом(1 и 2 режимы)')
print('есть 3 режима 1 сложение, 2 вычитание, 3 обычный')
rezhim = int(input('1 режим, 2 или 3: '))

number = random.randint(1, 20)
win = False

if rezhim == 1:
    for i in range(6):
        print('попытка номер', i)
        ans = int(input('введите 1 число: '))
        print('                 +')
        ans_2 = int(input('введите 2 число: '))
        otvet = ans + ans_2   
        if otvet == number:
            win = True
            break
        elif otvet < number:
            print('число больше')
        else:
            print('число меньше')

    if win:
        print('вы выйграли')
    else:
        print('вы проиграли')
        print('правильный ответ: ', number)

elif rezhim == 2:
    for i in range(6):
        print('попытка номер', i)
        ans = int(input('введите 1 число: '))
        print('                 -')
        ans_2 = int(input('введите 2 число: '))
        otvet = ans - ans_2   
        if otvet == number:
            win = True
            break
        elif otvet < number:
            print('число больше')
        else:
            print('число меньше')

    if win:
        print('вы выйграли')
    else:
        print('вы проиграли')
        print('правильный ответ: ', number)

elif rezhim == 3:
    for i in range(6):
        print('попытка номер', i)
        ans = int(input('введите 1 число: '))
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

else:
    print('bruh')