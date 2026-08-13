pizzas = ['hawaii', 'chicken', 'salami']
friend_pizzas = pizzas[:]

pizzas.append('cheese')
friend_pizzas.append('beef')

print('my favorite pizzas are: ')
for i in pizzas:
    print(i)

print("my friends' favorite pizzas are: ")
for k in friend_pizzas:
    print(k)
