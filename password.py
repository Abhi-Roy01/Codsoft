import random
import string

def generate_password(length):
    """
    Generate a random password of the specified length
    using a combination of uppercase and lowercase letters, digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """
    Main function to prompt the user for the desired password length
    and generate a password of that length.
    """
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))
    
    password = generate_password(length)
    print("Generated Password: ", password)
    main()