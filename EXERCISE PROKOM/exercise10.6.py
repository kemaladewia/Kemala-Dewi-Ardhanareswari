print("Give me two numbers, and I'll add them.") 

first_number = input("\nFirst number: ") 
second_number = input("Second number: ") 

try: 
    answer = int(first_number) + int(second_number) 
except ValueError: 
    print("Sorry, I can only add numbers. Please enter whole numbers only.") 
else: 
    print(f"{first_number} + {second_number} = {answer}")