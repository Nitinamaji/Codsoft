import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        print("Password length must be at least 1.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    generated_password = generate_password(
        length=password_length,
        use_uppercase=include_uppercase,
        use_digits=include_digits,
        use_special_chars=include_special_chars
    )

    if generated_password:
        print("\nGenerated Password:", generated_password)
