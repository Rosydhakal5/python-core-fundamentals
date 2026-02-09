#Purpose: Practice functions with inputs and modulo-based logic. 

def prime_checker(number):
    # 1 is not prime; prime numbers start from 2. 
    # This also handles zero and negative integers.
    if number < 2:
        print(f"{number} is not a prime number")
        return
    for i in range(2, number):
        if number % i == 0:
            print ("Not prime Number")
            return
    print ("Prime Number")
# Get user input and convert to integer for calculation
number = int(input("Enter a number\n"))
prime_checker(number)