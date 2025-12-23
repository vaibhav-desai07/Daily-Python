# Q2
x = int(input("Enter a number: "))
print("Even" if x%2==0 else "Odd")

# Q3
print("Enter three numbers: ")
x, y, z = int(input()), int(input()), int(input())
if x>y and x>z:
    print(x, "is greater!")
elif y>z:
    print(y, "is greater!")
else :
    print(z, "is greater!")