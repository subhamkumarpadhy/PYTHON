#Loops in python
#while loop
# count = 1 #it is an iterator
# while count <= 5 :
#     print("Hello")
#     count += 1

#print 1 - 5
# i = 1
# while i <= 5 :
#     print(i)
#     i += 1
# print("Loop ended")

#Some practice problems using while loop

#print from  1 - 100
# i = 1
# while i <= 100 :
#     print(i)
#     i += 1

#print from  100 - 1
# i = 100
# while i >=1 :
#     print(i)
#     i -= 1

#print multiplication table of a number n
# i = 1
# num = int(input("Enter the number:- "))
# while i <= 10 :
#     print(num * i)
#     i += 1

#Print the elements of lists using loop
# i = 0
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# while i <= len(nums) - 1 :
#     print(nums[i])
#     i += 1

#Search the element in the tuple using loop
# i = 0
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num_to_find = 36
# while i <= len(nums) - 1: 
#     if(nums[i] == num_to_find) :
#         print(num_to_find, "is present in the tuple at the index of ", i)
#     else :
#         print(num_to_find, "is not present in the tuple")
#     i += 1

#Break keyword 
# i = 1
# while i <= 5 :
#     print(i)
#     if(i == 3) :
#         break
#     i += 1
# print("Loop ended")

#Another example for break 
# i = 0
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# num_to_find = 36
# while i <= len(nums) - 1: 
#     if(nums[i] == num_to_find) :
#         print(num_to_find, "is present in the tuple at the index of ", i)
#         break
#     else :
#         print(num_to_find, "is not present in the tuple")
#     i += 1
# print("Loop end")

#Continue keyword
# i = 0
# while i <= 5 :
#     if(i == 3) :
#         i += 1
#         continue #skip the iteration
#     print(i)
#     i += 1
# print("Loop ended")

#printing only odd numbers
# i = 1
# while i <= 10 :
#     if(i % 2 == 0) :
#         i += 1
#         continue
#     print(i)
#     i += 1
# print("Loop ended")

#For loop in python
# vegatables = ["Aubergine", "Asparagus", "Cucumber", "Ladyfinger", "Sprouts", "Cabbage", "Potato", "Tomato"]
# for name in vegatables:
#     print(name)

#another example
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# for val in tup :
#     print(val)

#another example
# str = "RanjanSahu"
# for char in str :
#     print(char)

#some practice questions using for loop

#Print the elements of lists using loop
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for val in nums:
#     print(val)

#Search the element in the tuple using loop
# find_num = 81
# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# for num in nums:
#     if(num == find_num):
#         print(find_num, "is available.")
#         break
# else :
#     print(find_num, "is not available.")

#range() in python:- it returns a sequence of numbers, starting index = 0(default) ans increment by 1(default) & stops before specified num.
#range(start?, stop, stepsize?) #syntax

# print(range(7))
# for i in range(7): #stop condition given
#     print(i)
# for i in range(2, 8): #start & stop condition given
#     print(i)
# for i in range(4, 16, 4): #start, stop & step_size condition given
#     print(i)

#Some practice questions using range() & for loop

#print 1 - 100
# for i in range(1, 101, 1):
#     print(i)

#print 100 - 1
# for i in range(100, 0, -1):
#     print(i)

#print the multiplication table of num n
# num = int(input("Enter number:- "))
# for i in range(1, 11):
#     print(num * i)

#pass statement:- it is a null statement that does nothing. Used for writing future codes.
# for i in range(5):
#     pass
# print("Necessary work")

#some practice questions

#sum of first 'n' natural nums using while loop
# i = 1
# sum = 0
# n = int(input("Enter last digit:- "))
# while i <= n:
#     sum += i
#     i += 1
# print(sum)

#Find factorial of first 'n' numbers using for loop
n = int(input("Enter number:- "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)