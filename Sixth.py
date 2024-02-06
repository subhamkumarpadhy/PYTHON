# Functions & Recursion

# Function defination
# def cal_fact(a, b) : #parameters
#     return a + b
# fact = cal_fact(2, 5) #function call; arguments
# print(fact)

# def print_hello():
#     print("Hello")
# print_hello()

# avg of 3 numbers
# def cal_avg(a, b, c):
#     return ((a + b + c) / 3)
# avg = cal_avg(55,99,74)
# print(avg)

# # Default Parameters:- assigning a default value, which is used when no argument is passed.
# def cal_prod(a = 1, b = 1): #The default value should be given from last side
#     print(a * b)
#     return a * b

# cal_prod()

# def cal_prod(a, b = 1):
#     return a * b

# cal_prod(6)


# Some practice questions

# Print the length of a list.(para = a list)
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def cal_length(numbers_list):
#     return len(numbers_list)
# length = cal_length(num_list)
# print(length)

# WAF to print the elements of a list in a single line.(para = a list)
# city_name = ["Delhi", "Mumbai", "Chennai", "Pune", "Bbsr", "Cuttack", "Berhampur"]
# def print_name(name_of_cities):
#     for items in name_of_cities:
#         print(items, end=" ")
# print_name(city_name)

# WAF to find the factorial of n
# n = int(input("Enter number:- "))
# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
# print(factorial(n))

#WAF to convert USD to INR
# n = int(input("How many dollars you want to convert into INR:- "))
# def converter(usd_val):
#     inr_val = usd_val * 83
#     return inr_val
# ans = converter(n)
# print("The converted money in INR is:-", ans, "rupees")

#Input one number, if odd return "odd" else return "even"
# number = int(input("Enter the number to check it is even or odd:-  "))
# def check_num(int):
#     if(int % 2 == 0):
#         print("Even")
#     else:
#         print("Odd")
# check_num(number)

#Recursion
# def show(n):
#     if(n == 0): #Base case
#         return
#     print(n)
#     show(n - 1)
# show(7)

#Find factorial with recursion
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n - 1) * n
# print(fact(5))

#Some practice problems

#Calculate sum of first natural number with recursion
# n = int(input("Enter the last digit of the natural number:- "))
# def cal_sum(last_digit):
#     if(last_digit == 0):
#         return 0
#     return cal_sum(last_digit - 1) + last_digit
# sum = cal_sum(n)
# print(sum)

#Print the elements of a list with recursion
my_fruits = ["Orange", "Apple", "Grape", "Banana", "Mango", "Strawberry", "Lemon"]
def print_fruit(list, idx = 0):
    if(len(list) == idx):
        return
    print(list[idx])
    print_fruit(list, idx + 1)
print_fruit(my_fruits)









