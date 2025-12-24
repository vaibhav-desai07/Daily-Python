# CONCEPTS
# Strings, Lists & Tuples

# Q1 Reverse a string
s = input("Enter a string: ")
rev = s[::-1]
print(rev)


# Q2 Count vowels in a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count+=1
print("Number of vowels:", count)


# Q3 Maximum and Minimum of a list
n  = int(input("Enter number elements: "))
lst = []

print("Enter elements: ")
for i in range(n):
    lst.append(int(input()))

print("Maximum :", max(lst))
print("Minimum :", min(lst))


# Q4 Check for Palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("Palindrome!")
else :
    print("Not a Palindrome!")