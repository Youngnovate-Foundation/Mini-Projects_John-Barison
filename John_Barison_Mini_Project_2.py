# PASSWORD GENERATOR
import random
import string

print("Welcome to the Password Generator!")
def password_gen():
    while True:
        try:
            length = int(input("How long do you want your password to be? "))
            break
        except ValueError:
            print("Please enter a number.")
    choice = input("Do you want to include special characters? (yes/no): ").lower()
    if choice == 'yes':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits
    gen_password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Your generated password is: {gen_password}")

password_gen()