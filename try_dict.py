cats = {
    'red': 2,
    'black': 5,
    'white': 3
}
cats['white'] = cats['white'] + 1
cats['red'] += 1

print(cats)


kirill_cats = {
    'black':1,
    'green':1
}

kirill_cats['white'] = 1
kirill_cats['black'] += 2

print(kirill_cats)

print(cats.keys())
print(kirill_cats.keys())

all_keys = list(cats.keys()) + list(kirill_cats.keys())

all_cats = {}

for key in all_keys:
    my_cats = cats[key] if key in cats else 0
    k_cats = kirill_cats[key] if key in kirill_cats else 0
    all_cats[key] = my_cats + k_cats

for color in ['white', 'black', 'red', 'green']:
    print(color)

print(all_cats)