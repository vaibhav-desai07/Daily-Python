# CONCEPTS
# Functions(Definition, Arguments, Return Values, Default & Keyword Arguments), Import, Buit-in Modules(Math, Random, Datetime), PIP

# Q1 Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True
   
n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

# Q2 Function for factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))

# Q3 Using random. to create a number guessing game
import random
secret = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))  
    if guess == secret:
        print("Wow Correct guess!")
        break
    else:
        print("Wrong guess, try again!")

# Q4 Created a module file (mymodule.py)
import mymodule

print(mymodule.add(10, 5))
print(mymodule.sub(10, 5))