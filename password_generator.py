import random
import string
def password_generator():
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase? (y/n): ").lower() == 'y'

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = "".join(random.choice(characters) for _ in range(length))
    print(f"Generated password: {password}")

password_generator()