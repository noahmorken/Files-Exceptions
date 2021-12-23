import json

def get_stored_number():
    """Get stored number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number():
    """Prompt for a new number."""
    number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number

def remember_number():
    """Tells the user their favorite number."""
    number = get_stored_number()
    if number:
        print(f"I know your favorite number! It's {number}!")
    else:
        number = get_new_number()
        print(f"Your favorite number's been saved!")

remember_number()