# CONCEPTS
# Operators(Arithmetic, Relational, Logical) & Expressions

# Q1 Calculator using user input

# Q2 Check Even or Odd
x = int(input("Enter a number: "))
print("Even" if x%2==0 else "Odd")

# Q3 Largest of three
print("Enter three numbers: ")
x, y, z = int(input()), int(input()), int(input())
if x>y and x>z:
    print(x, "is greater!")
elif y>z:
    print(y, "is greater!")
else :
    print(z, "is greater!")