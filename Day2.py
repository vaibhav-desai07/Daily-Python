# Q1 Take user input and display its type
x = input()
print(type(x))

# Q2 Convert string input into integer and perform addition
y = input()
y = int(y)
print(y+2)

# Q3 Swap two vars (with and without temp var)
a = 2
b = 3
print("Before")
print("a =",a,"b =",b)
#with temp
temp = a
a = b
b = temp
print("With temp")
print("a =",a,"b =",b)

# without temp
a, b = b, a
print(a, b)