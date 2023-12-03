import random

def super_secret():
    secret = random.randint(1, 10)
    if secret == 5:
        print('ласт кристмас. ай гед ю ма харт. бат зе вери некст дей ю гейв и тебей. зыс еа ай гейминг фор тиз энд ай гив ю самвон спешл :3')
    elif secret == 1 or secret == 10:
        print('нового года не будет. дед мороз принял ислам')
    elif secret == 2 or secret == 8:
        print('новый год будет. дед мороз принял христианство вновь')
    elif secret == 3 or secret == 7:
        print('новый год скоро')
    elif secret == 4 or secret == 6:
        print('новый год супер скоро))')