# Q1
x = input()
print(type(x))

# Q2
y = input()
y = int(y)
print(y+2)

# Q3
a = 2
b = 3
#with temp
temp = a
a = b
b = temp
print("With temp")
print("a =",a,"b =",b)

# without temp
a, b = b, a
print(a, b)