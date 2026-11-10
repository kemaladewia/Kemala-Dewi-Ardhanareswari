from random import choice

def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []


    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    """Check all elements in the played ticket. If any are not in the
    winning ticket, return False.
    """
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    return True

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [5, 'a', 9, 'c']

plays = 0
won = False
 
max_tries = 1_000_000

while not won:
    new_ticket = get_winning_ticket(possibilities)
    won = check_ticket(my_ticket, new_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning ticket: {new_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {my_ticket}")
    print(f"Last attempt: {new_ticket}")