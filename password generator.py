import random
import string

def generate_strong_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Define character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Ensure at least one character from each category
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with a mix of all character sets
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Example usage
print("Your strong password is:", generate_strong_password(16))


