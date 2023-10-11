import viselnizha_words

print('игра висельница')
guess_limit = 25
guessed_letters = []
print('есть', guess_limit, 'попыток')

word = viselnizha_words.get_random_word()

def hide_word(word, letters = []):
    res = ''

    for w in word:
        if w in letters:
            res += '['+ w + ']'
        else:
            res += '[_]'
    return res

def word_match(word, letters = []):
    for w in word:
        if w in letters:
            pass
        else:
            return False
    return True

for i in range(guess_limit):
    print('попытка №', i)
    letter = input('напиши букву: ')
    guessed_letters.append(letter)
    hidden_word = hide_word(word, guessed_letters)
    print(hidden_word)
    print('использованные буквы:', ','.join(guessed_letters))
    if word_match(word, guessed_letters):
        print('ай маладес')
        break

print('правильное слово: ', word)
