from pathlib import Path 

filenames = ('EXERCISE PROKOM/cats.txt, EXERCISE PROKOM/dogs.txt')

for filename in filenames: 
    print(f"\nReading file: {filename}") 
    
    path = Path(filename) 
    try: 
        contents = path.read_text() 
    
    except FileNotFoundError: 
        print(f"  Sorry, I can't find the file {filename}.") 
    else: 
        print(contents.rstrip())