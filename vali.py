import re

email = input("Enter your email: ")
password = input("Enter your password: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*?]).{8,}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email Format")

if re.match(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password! Must contain:")
    print("- At least 8 characters")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one digit")
    print("- At least one special character (@#$%&!*?)")
