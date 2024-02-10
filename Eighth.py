#OOPs in python

#Creating a class
# class Student:
#     name = "samir"

#Creating an object
# s1 = Student()
# print(s1)
# print(s1.name)

##Creating another object of same class Student
# s2 = Student()
# print(s2.name)

#Creating another class
# class Car:
#     colour = "Black"
#     brand = "MAHINDRA & MAHINDRA"

# car1 = Car()
# print(car1.colour)
# print(car1.brand)

# Constructor or __init__() in python
#All classes have a function called __init__(), which is always executed when the object is being initiated.
# class Student:
#     name = "samir"

    #default constructor
    # def __init__(self): #Every method should have "self" as it's argument otherwise it wil give error.
    #     pass

    #Parameterized constructor
#     def __init__(self, name,  marks): #Here the parameter "self" is pointing to the "s1" object only, ie:- in memory both "s1" & "self" are pointing to the same memory location.
#         self.name = name
#         self.marks = marks
#         print("Adding new student in the Database......")

# s1 = Student("Ranjan", 56)
# print(s1.name, s1.marks)

# s2 = Student("Krishna", 76)
# print(s2.name, s2.marks)

#Q. Create Student class, input - name & marks of 3 subjects in constructor, then a method to print their average

# class Student:
#     def __init__(self, name, marks): #Assuming marks are in list
#         self.name = name
#         self.marks = marks

#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg marks is:" , sum / 3 )

# s4 = Student("Barun", [96, 87, 91])
# s4.avg_marks()

#Static Methods:- Methods that doesn't use the self parameter(Work at class level)
# class Student:
#     @staticmethod #It is a decorator
#     def hello():
#         print("Hello")
# Student.hello() #As it works on class level so without creating object we can directly call it with it's class name.

#Abstraction:- Hiding the implementation details of a class & only showing the essential features to the user.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
#     def start(self):
#         self.cluthch = True
#         self.acc =  True
#         print("Car is started.")
# c1 = Car()
# c1.start() #prints only the necessary part by hiding the internal details, which are ususlly not need to the user.

#Encapsulation:- Wrapping data & functions into a single unit(onject).

#Q. create class Account with attributes (balance, account no.) & methods for debit, credit & print the balance.
class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        self.balance -= amount
        print(amount, "rupees is debited.")
    def credit(self, available):
        self.balance += available
        print(available, "rupees is credited.")


    def get_balance(self):
        print("The available balance is:", self.balance)
        
acc1 = Account(100000, 3124567854)
print("Person one details:-")
print("The person with account number", acc1.account_number, "has the balance", acc1.balance)
acc1.credit(50000)
acc1.debit(4523)
acc1.credit(2000)
acc1.debit(500)
acc1.get_balance()
print("\n")
print("Person two details:-")
acc2 = Account(10000000, 3215465428)
print("The person with account number", acc2.account_number, "has the balance of", acc2.balance)
acc1.credit(8547)
acc1.debit(5348)
acc1.credit(6042)
acc1.debit(756)
acc1.get_balance()