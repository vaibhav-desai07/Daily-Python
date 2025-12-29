# CONCEPTS
# OOPs (Class & c1ects, INIt, Methods, Encapsulation, Inheritance, Polymorphism, Method Overriding)

# Q1 Parent-child class example.
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

c1 = Child()
c1.show_parent()
c1.show_child()

# Q2 Create a Student class.
class Student:
    college_name = "JP University"
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("adding new student in database...")
    

s1 = Student("ram", 98)
print(s1.name, s1.roll)
s2 = Student("hero",  99)
print(s2.name, s2.roll)
print(Student.college_name)

# Q3 Bank account class.
class BankAccount:
    def __init__(self, balance, acc):
        self.__balance = balance  # private variable
        self.account_no = acc

    def credit(self, amount):
        self.__balance += amount
        print("Rs.", amount, "was credited!")

    def show_balance(self):
        print("Balance:", self.__balance)

    def debit(self, amount):
        self.__balance -= amount
        print("Rs.", amount, "was debited!")

acc1 = BankAccount(1000,12345)
acc1.show_balance()
acc1.credit(500)
acc1.show_balance()
acc1.debit(500)
acc1.show_balance()



# Q4 Demonstrate constructor.
class Demo:
    def __init__(self):
        print("Constructor is called automatically")

c1 = Demo()