num = int(input("Enter a number: ")) 
factorial = 1 
for i in range(0, num + 1): 
    if i == 0: 
        pass 
    if i == 0: 
        continue 
    if i < 0: 
        print("Factorial not defined for negative numbers.") 
        break 
    factorial *= i 
else: 
    print("Factorial of num using for loop is:" ,factorial) # Factorial using WHILE loop 
n = num 
fact = 1 
i = 1 
while i <=n: 
    if i ==0: 
        pass 
    if i <0: 
        print("Invalid input!") 
        break 
    if i == 0: 
        continue 
    fact *= i 
    i += 1 
else: 
    print("Factorial of num using while loop is:",fact) 

 