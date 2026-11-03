prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you're finished: "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")