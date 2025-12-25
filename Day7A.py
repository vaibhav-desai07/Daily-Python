# CONCEPTS
# File Handling(Read/Write Files, Modes(r,w,a), With Statement) & Exception Handling(Try, Except, Finally, Custom Exceptions)

# Q1 Write & Read data to a file.
f = open("sample.txt","w")
f.write("\nThe day is so beautifull, isn't it.")

f = open("sample.txt","r")
data = f.read()
print(data)
f.close()

# Q2 Copy contents from one file to another.
with open('sample.txt','r') as firstfile, open('second.txt','w') as secondfile:
    data = firstfile.read()
    secondfile.write(data)

# Q3 Handle division by zero.
num = 10
zero = 0

try:
    result = num / zero
    print("The result is: ",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    result = None 

# Q4 Raise custom exception.
x = int(input("Enter a Odd Number: "))
if x%2 == 0:
    raise Exception("Sorry!, Only Odd numbers are allowed")