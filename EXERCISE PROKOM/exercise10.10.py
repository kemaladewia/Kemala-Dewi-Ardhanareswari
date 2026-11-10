from pathlib import Path 

def count_common_words(path, word): 
    """Count how many times word appears in the text.""" 
    
    try: 
        contents = path.read_text(encoding='utf-8') 
    except FileNotFoundError: 
        print(f"Sorry, the file {path} does not exist.") 
    else: 
        word_count = contents.lower().count(word) 
        
        msg = f"'{word}' appears in {path} about {word_count} times." 
        print(msg) 
        
    filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt'] 
    
    for filename in filenames:
        path = Path(filename) 
        count_common_words(path, 'the') 
        count_common_words(path, 'the ') 
        print()