__author__ = 'tocando'

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

print '-' * 20
print 'now for a more pythonic way'
for rabbit in rabbits:
    print(rabbit)

print '-' * 20
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    if accusation[card] == 'ballroom':
        print(card)
    else:
        continue

print 'did you find room?'
print 'now for the values'
for value in accusation.values():
    print(value)

print '-' * 20
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

print '-' * 20

cheeses = []
for cheese in cheeses:
    print("this shop has some lovely", cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

print '-' * 20
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

print '-' * 20
spanish = ['Lunes', 'Martes', 'Miercoles']
print "the list is: ", list(zip(days, spanish))
print '-' * 20
print 'dict is: ', dict(zip(days, spanish))

print '-' * 20
for x in range(10, -1, -1):
    print(x)

