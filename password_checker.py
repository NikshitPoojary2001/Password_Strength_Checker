# password strength checker

# password strength check conditions:
# min 8 chars, digit, uppercase, lowercase, special characters

import re

def password_strength_checker(password):
    if len(password) < 8:
        return "Weak: Password must be atleast 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain an uppercase character"
    
    if not any(char.islower() for char in password):
        return "Weak: Password must contain an lowercase character"
    
    if not re.search(r'[!@#$%^&*()<>.?]',password):
        return "Medium: Password must contain a special character"
    
    return "Strong: Your Password is Secured!"

def password_checker():
    print("Welcome to the Password Strength Checker")

    while True:
        password = input("Enter your Password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Thank you for using this tool")
            break

        result = password_strength_checker(password)
        print(result)

# Run Password Checker

if __name__ == "__main__":
    password_checker()
    
