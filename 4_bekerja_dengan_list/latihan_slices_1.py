item_ku = ['hp', 'laptop', 'buku', 'pensil', 'tas']

print(item_ku[0:3])
#print 3 item awal dari list

print(item_ku[1:4])
#print 3 item di tengah list

print(item_ku[2:5])
#print 3 item terakhir dari list

pizzas = ['pizza hut', "domino's", "papa ron's"]

friend_pizzas = pizzas[:]

pizzas.append('ntah pizza apa')
friend_pizzas.append('pizza temen apa')

for pizza in pizzas:
    print(pizza.title())
for pizza in friend_pizzas:
    print(pizza.title())

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('\n')
for food in my_foods:
    print(food)
    
for food in friend_foods:
    print(food)