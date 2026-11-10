from pathlib import Path 

print("Enter 'quit' when you are finished.") 

names = [] 
while True: 
    name = input("\nWhat's your name? ") 
    if name == 'quit': 
        break 
    
    print(f"Thanks {name}, we'll add you to the guest book.") 
    names.append(name) 
    

contents = '' 
for name in names: 
    contents += f"{name}\n" 
    
path = Path('guest_book.txt') 
path.write_text(contents)