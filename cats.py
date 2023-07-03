class Cat:
    def __init__(self, name, age, tail_length):
        self.name = name
        self.age = age
        self.tail_length = tail_length

    def __str__(self):
        return 'Cat {0}, {1}, {2}'.format(self.name, self.age, self.tail_length)

def create_cat():
    print('creating cat')
    n = input('name: ')
    a = input('age: ')
    t = input('tail_length: ')
    cat = Cat(n, a, t)
    return cat

tihon = Cat('Tihon', 13, 20)
plushka = Cat('Plushka', 1, 15)
cats = []
while True:
    cat1 = create_cat()
    cats.append(cat1)
    answer = input('create another cat? Yes/No: ')
    if answer.lower() == 'no':
        break

print(cats)