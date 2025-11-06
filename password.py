import re
password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
print(type(password_pattern))

passwords = ["Hello123!","Weakpass","Strongpass@2003"]

for pw in passwords:
    if password_pattern.match(pw):
        print("Valid Password",pw) 
    else:
        print("Invalid Password",pw)       
