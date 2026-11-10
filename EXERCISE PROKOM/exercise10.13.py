from pathlib import Path 
import json  

def get_stored_user_info(path): 
    """Get stored user info if available.""" 
    if path.exists(): 
        contents = path.read_text() 
        user_dict = json.loads(contents) 
        return user_dict 
    else: 
        return None

def get_new_user_info(path): 
    """Get information from a new user.""" 
    username = input("What is your name? ") 
    game = input("What's your favorite game? ") 
    animal = input("What's your favorite animal? ") 
    
    user_dict = { 
        'username': username, 
        'game': game, 
        'animal': animal, 
        } 
    contents = json.dumps(user_dict) 
    path.write_text(contents) 
    return user_dict 

def show_user_info(user_dict): 
    """Print a summary of exactly what we remember about the user.""" 
    print("\nHere's what we remember about you:") 
    print(f"  Name: {user_dict['username']}") 
    print(f"  Favorite game: {user_dict['game']}") 
    print(f"  Favorite animal: {user_dict['animal']}") 
    
def greet_user(): 
    """Greet the user by name, and summarize what we know about them.""" 
    path = Path('user_info.json') 
    user_dict = get_stored_user_info(path) 
    
    if user_dict: 
        print(f"Welcome back, {user_dict['username']}!") 
    else: 
        get_new_user_info(path) 
        # Read the information back in from the file, so the summary 
        # # shows exactly what was stored. 
        user_dict = get_stored_user_info(path) 
        print(f"\nWe'll remember you when you come back, " 
              f"{user_dict['username']}!") 
        show_user_info(user_dict) 
        
greet_user()