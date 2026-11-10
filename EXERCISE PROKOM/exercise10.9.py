from pathlib import Path 

filenames = ['EXERCISE PROKOM/cats.txt', 'dogs.txt'] 

for filename in filenames: 
    path = Path(filename) 
    try: 
        contents = path.read_text() 
    except FileNotFoundError: 
        pass 
    else: 
        print(f"\nReading file: {filename}") 
        print(contents.rstrip())