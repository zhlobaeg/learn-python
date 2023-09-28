print('игра висельница')
word = input('загадай слово: ')

letter = input('напиши букву: ')

def hide_word(word, letter = None):
    res = ''

    for l in word:
        if l == letter:
            res += '['+ l + ']'
        else:
            res += '[_]'
    return res


    
print(hide_word(word, letter))