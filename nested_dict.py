busket1 = {
    'apple': 10,
    'pear': 8,
    'pineapple': 2
}
#print(busket1['pear'])

busket1['cherry'] = 10
busket1['apple'] += 2

busket2 = {
    'cucumber': 2,
    'tomato': 3,
}

busket2['cucumber'] += 2
busket2['pumpkin'] = 1

#print(busket2['cucumber'])

purchases = {
    'vegetebles': busket2,
    'fruits': busket1
}
#print(purchases['vegetebles']['cucumber'])

purchases['fruits']['apples'] = 1

list1 = [busket1, busket2]
list1[1]['pumpkin'] += 1
#print(list1[0])
#print(list1[1])
#print(purchases)

colors = ['red', 'green', 'blue']
sizes = ['big', 'medium', 'small']

#print(colors[0],sizes[1])

properties = {
    'colors': colors,
    'sizes': sizes,
    'height': 100
}
print(properties['colors'][2])