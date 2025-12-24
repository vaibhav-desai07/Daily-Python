# Q1 Word frequency calculator
sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

# Q2 Students marks dictionary
students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print(students)

# Q3 Find common elements using sets
set1 = {1,2,3,4,5}
set2 = {8,6,4,1,2,5}

common = set1.intersection(set2)

print("Common elements:", common)