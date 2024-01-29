#Lists in python
# marks = [54.5, 45.6, 89.4, 57.5, 96.4] #syntax
# details = ["karan", 94.5, 23, "sasanpadar"]
# print(marks)
# print(type(marks))
# print(details)

# #lists are mutable but strings are immutable in python
# details[0] = "kanha"
# print(details)

#List slicing is similiar to string slicing
# nums = [54, 85, 96, 45, 77, 63]
# print(nums[2:5])
# print(nums[-4:-1])#-ve slicing

#Lists Methods
# marks = [54, 63, 96, 85, 67, 94, 100]
# name = ["apple", "subham", "aeroplane", "khusi", "ankita"]
# nums = [1, 5, 8, 9, 5, 1, 2, 7]
#The methods return None value 
# print(marks.append(50)) # It add the value at last
# print(marks)
# print(marks.sort()) #It sort the list in ascending order
# print(marks)
# print(marks.sort(reverse=True)) #It sort the list in decending order
# print(marks)
# print(name.sort())
# print(name)
# print(name.sort(reverse=True))
# print(name)
# print(marks.reverse()) #It totally reverse the original list
# print(marks)
# print(marks.insert(2, 20)) #Insert at a perticular index
# print(marks)
# print(nums.remove(5)) #removes first occurance of element
# print(nums)
# print(nums.pop(6)) #remove the element at given index & return which element is removed
# print(nums)

#Tuples in python:- Tuples are immutable in python & very much similiar to list
# tup = (45, 68, 74, 21, 98, 23)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# print(tup[2])

#we can't do 
# tup[0] = 45 #it will show error

#an empty tuple
# tup = ()
# print(tup)
# print(type(tup))

#Syntax of tuple with only single element
# tup = (1,)
# print(tup)
# print(type(tup))

#We can do slicing in tuple also, similiar to string & list
# var = (67,78,654,45,657,55,67)
# print(var[2:5])

#Methods in Tuple
# tup = (4, 5, 8, 4, 6, 9, 3, 6, 4, 8, 9)
# print(tup.index(9)) #returns index of first occurrence
# print(tup.count(4))#counts total occurrence

#some practice problems

#input 3 movie & store in list
# movie1 = input("Enter first movie: ")
# movie2 = input("Enter second movie: ")
# movie3 = input("Enter third movie: ")
# movies = [movie1, movie2, movie3]
#OR
# movies = []
# movies.append(input("Enter first movie: "))
# movies.append(input("Enter second movie: "))
# movies.append(input("Enter third movie: "))
# print(movies)

#check list contains a palindrome of elements or not
# list1 = [1, 2, 1]
# list2 = [1, 2, 3]
# list1_copy = list1.copy()
# list1_copy.reverse()
# if(list1_copy == list1):
#     print("List is palindrome")
# else:
#     print("List is not palindrome")

# list2_copy = list2.copy()
# list2_copy.reverse()
# if(list2_copy == list2):
#     print("List is palindrome")
# else:
#     print("List is not palindrome")

#Count number of occurrence of a tuple
# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))

#store the above tuple in a list and sort them in ancending
# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)