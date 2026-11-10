from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f" Pulled: {pulled_item}")
        winning_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_ticket}")
print("Any ticket matching these 4 numbers or letters wins a prize!")