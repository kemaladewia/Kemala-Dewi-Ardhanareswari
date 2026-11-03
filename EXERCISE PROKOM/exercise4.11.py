pizzas = ['pepperoni', 'magharita', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('beef')
friend_pizzas.append('chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend favorite pizzas are: ")    
for pizza in friend_pizzas:
    print(pizza)