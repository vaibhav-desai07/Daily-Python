# CONCEPTS
# Conditional Statements(If, Elif, Else, Nested Conditions) & Loops(For, While) & (Break, Continue & Pass)

# Q1 Grade calculatoer based on marks
marks = int(input("Enter your marks: "))
if marks > 90:
    print("Grade - A")
elif marks > 80:
    print("Grade - B")
elif marks > 70:
    print("Grade - C")
elif marks > 60:
    print("Grade - D")
elif marks >= 50:
    print("Grade - E")
else :
    print("Grade - F")

# Q2 Electricity bil calculator
units_consumed = int(input("Enter units consumed: "))
rate_per_kwh  = 6 #in rupees
energy_charge = units_consumed * rate_per_kwh
fixed_charge = 100
tax = 0.05 * ( energy_charge + fixed_charge ) # 5% gst
total_bill = energy_charge + fixed_charge + tax
print("Your Total Bill is", total_bill, "Rupees")

# Q3 Print first N natural numbers
x = int(input("Enter no. of natural numbers: "))
i = 1
while i <= x:
    print(i, end=" ")
    i+=1

# Q4 Factorial of a number
x = int(input("Enter a number for factorial: "))
i = 1
while x != 0:
    i = i * x
    x -= 1
print("Factorial is", i)