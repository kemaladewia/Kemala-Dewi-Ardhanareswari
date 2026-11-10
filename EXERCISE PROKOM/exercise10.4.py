from pathlib import Path 

name = input("What's your name? ") 

path = Path('guest.txt') 
path.write_text(name) 

print(f"Thanks {name}, we'll be sure to remember you.")