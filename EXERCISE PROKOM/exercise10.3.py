from pathlib import Path 

path = Path('EXERCISE PROKOM/pi_digits.txt') 
contents = path.read_text() 

#for line in contents.splitlines(): 
    
    # print(line)

pi_string = '' 
for line in contents.splitlines(): 
    pi_string += line.lstrip() 
    
# print(pi_string) 
# print(len(pi_string))
print(f"{pi_string[:52]}...") 
print(len(pi_string))