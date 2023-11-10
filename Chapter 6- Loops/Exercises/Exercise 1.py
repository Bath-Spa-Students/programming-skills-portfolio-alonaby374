text = "\nWhat topping would you like on your pizza?"
text += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(text)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break