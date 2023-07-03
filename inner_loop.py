class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Human {self.name}, {self.age}'
    
class House:
    def __init__(self, number, tenants):
        self.number = number
        self.tenants = tenants

        


house1 = House(1, [Human('Вася', 15), Human('Петя', 18), Human('Катя', 10)])
house2 = House(2, [Human('Гриша', 37), Human('Кирилл', 14), Human('Настя', 20)])
house3 = House(3, [Human('Ксюша', 5), Human('Андрей', 6), Human('Соня', 50), Human('Слава', 16)])

street = [house1, house2, house3]

def  count_street(street):
    num_people = 0
    for house in street:
        num_people += len(house.tenants)
    return num_people

def count_dom_age(house):
    total_age = 0
    for human in house.tenants:
        total_age += human.age
    return total_age

def count_street_age(street):
    total_age = 0
    for house in street:
        for human in house.tenants:
            total_age += human.age
    return total_age

def show_street(street):
    for house in street:
        for human in house.tenants:
            print(human.name)
            
show_street(street)