# "del" keyword in python is used to delete obj properties or obj itself.
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("Kanha")
# print(s1.name)
# del s1.name
# print(s1.name)


#Private(like) attributes & methods in python:- we can made any method or attribute a private member with the help of 2 underscores(__).
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass# we can't access it outside of the class, we can access it within the class only.

#     def reset_pass(self):
#         print(self.__acc_pass)#use of private member within the class

#     def __hello(self, name):#can't access it outside of the class as it a private method.
#         self.name = name

# acc1 = Account("542614", "krishna")
# print(acc1.acc_no)
# acc1.reset_pass()#can access it coz it is not a private method.
# print(acc1.__acc_pass)#can't access it outside the class


#Inheritance
# class Car:
#     color = "Black"
#     @staticmethod 
#     def start():
#         print("Car is started...")

#     @staticmethod
#     def stop():
#         print("Car stops.")

# class Land_Rover(Car):#use of inheritance
#     def __init__(self, name):
#         self.name = name

# car3 = Land_Rover("Discovery")
# car4 = Land_Rover("Defender")
# car5 = Land_Rover("Range_Rover")

# car3.start()
# print(car3.name)
# print(car4.name)
# print(car5.name)
# print(car5.color)
# car3.stop()


#super() in python is used to access methods of the parent class.
# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod 
#     def start():
#         print("Car is started...")

#     @staticmethod
#     def stop():
#         print("Car stops.")

# class Land_Rover(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car3 = Land_Rover("Defender 110", "Electric")
# print(car3.type)


#class method:- is bound to the class & receives the class as an implict first argument.
# class Person:
#     name  = "barun"
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p2 = Person()
# p2.changeName("aditya")
# print(p2.name)
# print(Person.name)


#Property decorator:- we use it on any method in the class to use the method as a property.
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stud2 = Student(60, 66, 90)
# print(stud2.percentage)
# stud2.phy = 81
# print(stud2.percentage)


#Polymorphism: Operator Overloading (Dunder function)
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +", self.img,"j")

#     def __add__(self, num2):#Dunder function
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)

#     def __sub__(self, num2):#Dunder function
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)

# num1 = Complex(5, 9)
# num1.showNumber()

# num2 = Complex(6, 5)
# num2.showNumber()

# num3 = num1 + num2
# num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()


#Some practice problems

#Create a class Circle with a constructor having radius & 2 methods to calculate it's area & perimeter.
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return (self.radius * self.radius * 3.14)

#     def perimeter(self):
#         return (2 * self.radius * 3.14)

# c1 = Circle(5)
# print(c1.area())
# print(c1.perimeter())


#Inheritance problem
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("The role is:", self.role)
#         print("The department is:", self.department)
#         print("The salary is:", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "Civil", 40000)

#     def showDetail(self):
#         print('\n')
#         super().showDetails()
#         print("The name is:", self.name)
#         print("The age is:", self.age)

# emp1 = Employee("Software Engineer", "Android", 50000)
# emp1.showDetails()
# emp2 = Engineer("Sritam", 23)
# emp2.showDetail()


#use of dunder function __gt__
# class Order:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, ord2):
#         return self.price > ord2.price

# ord1 = Order("Kurkure", 1000)
# ord2 = Order("Coffee", 100)
# print(ord1 > ord2)