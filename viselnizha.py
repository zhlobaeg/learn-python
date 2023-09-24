print('игра висельница')
word = input('загадай слово: ')

def hide_word(word):
    res = ''
    for i in range(len(word)):
        res += '[_]'
    return res
    
print(hide_word(word))