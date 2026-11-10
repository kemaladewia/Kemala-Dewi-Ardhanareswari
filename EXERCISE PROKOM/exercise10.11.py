from pathlib import Path 
import json 

# number = input("What's your favorite number? ") 

# path = Path('favorite_number.json') 
# contents = json.dumps(number) 
#  path.write_text(contents) 

path = Path('favorite_number.json') 
contents = path.read_text() 
number = json.loads(contents)

# print("Thanks! I'll remember that.")
print(f"I know your favorite number! It's {number}.")