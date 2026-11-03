my_food = ['nasgor', 'naspad', 'naskuning', 'nasuduk']
friend_food = my_food[:]

my_food.append('ayam')
friend_food.append('ikan')

print("My foods:")
for food in my_food:
    print(food)

print("\nMy friend foods:")   
for food in friend_food:
    print(food)