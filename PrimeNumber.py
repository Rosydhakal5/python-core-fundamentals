# Purpose: Practice functions with inputs and modulo-based logic. 
import math

def prime_checker(number):
    # 1 is not prime; prime numbers start from 2. 
    # This also handles zero and negative integers.
    if number <= 1: 
        return "Natural number, Not Prime"
    
    if number == 2 or number == 3: 
        return "Prime Number"
    
    if number % 2 == 0 or number % 3 == 0: 
        return "Not Prime"

    # Using 6K +-1 rule for optimization 
    for i in range(5, int(math.sqrt(number) + 1), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return "Not Prime"
    
    return "Prime"

# Get user input and convert to integer for calculation
user_input = int(input("Enter a number: "))
result = prime_checker(user_input)
print(result)