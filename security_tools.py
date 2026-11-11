
# Task 5 - Reusable Cyber Security Utilities
import random
import string



def validate_password(password):

    
    if len(password) < 8:
        return False

    
    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    
    if not any(char.isdigit() for char in password):
        return False

    
    if not any(char in string.punctuation for char in password):
        return False

    return True



def validate_ip(ip_address):

    
    ip_address = ip_address.strip()

    
    if ip_address.count(".") != 3:
        return False

    
    parts = ip_address.split(".")

    if len(parts) != 4:
        return False

    
    for part in parts:

        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True



def generate_password():

    
    password_length = random.randint(10, 16)

    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    
    all_characters = uppercase + lowercase + digits + symbols

    
    for i in range(password_length - 4):
        password.append(random.choice(all_characters))

    
    random.shuffle(password)

    # Convert the list into a string
    return "".join(password)
