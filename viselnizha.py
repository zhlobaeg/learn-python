import viselnizha_words

print('игра висельница')

word = viselnizha_words.get_random_word()

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
print(word)