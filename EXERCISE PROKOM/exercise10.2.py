from pathlib import Path 

path = Path('EXERCISE PROKOM/learning_python.txt') 
contents = path.read_text() 

for line in contents.splitlines(): 
    line = line.replace('Python', 'C') 
    print(line)