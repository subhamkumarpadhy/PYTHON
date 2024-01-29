#creation of string
# srt1 = "kanha padhy"
# str2 = 'kanha padhy'
# str3 = '''kanha padhy'''

#string concatenation & length
# str2 = 'kanha padhy'
# len1 = len(str2)
# print(len1)
# str3 = '''\nkanha padhy'''
# fstring = str2 + str3
# print(fstring)

#indexing in string
# str = "kanha padhy"
# print(str[4])
#with the help of index we can only access the character, but can't modify it a particular index.


#slicing in python
# syntax = str[starting_idx:ending_idx] #ending idx is not included
# str = "subham kumar padhy"
# print(str[4:10])
# print(str[4:len(str)]) #[4:last_idx]
# print(str[:10]) #[starting_idx:10]

#-ve indexing in python
# str5 = "apple"
# print(str5[-3:-1]) #counting start from backword ie:- elppa

#some string functions
#Any function in python does not change the original string, it creats a new string then change that string
# str = "i am a coder"
# print(str.endswith("er.")) #returns true if string ends with substr
# print(str.capitalize()) #capitalizes 1st char
# print(str.replace("a", "o")) #replaces all occurrences of old with new
# print(str.replace("coder", "army")) 
# print(str.find("c")) #returns 1st index of 1st occurrence
# print(str.find("am"))
# print(str.count("a")) #counts the occurrence of substr in string
# print(str.count("coder"))


#some practise questions on string

#input first name & print length
# str = input("Enter your first name: ")
# print(len(str))

#find occurrence of "S" in a string
# str = "hollas how are your days are gones"
# print(str.count("s"))


#Conditional statements in python
#if-elif-if(syntax)
# age = 19
# if(age > 18):
#     print("you can vote")
# elif(age == 18):
#     print("you can drive")
# else:
#     print("You can not vote")

#program to give grades using conditional statements
# marks = int(input("Enter your marks: "))
# if(marks >= 90):
#     print("Your Grade is A")
# elif(marks >= 80 and marks < 90):
#     print("Your Grade is B")
# elif(marks >= 70 and marks < 80):
#     print("Your Grade is C")
# else:
#     print("Your Grade is D")


# some practice questions

#check even or odd
# num = int(input("Enter a number: "))
# if(num % 2 == 0):
#     print("The number is even.")
# else:
#     print("The number is odd.")

#greatest of 3 numbers entered by user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if(num1 > num2 and num1 > num3):
#     print("The greatest number is ->" , num1)
# elif(num2 > num3):
#     print("The greatest number is ->" , num2)
# else:
#     print("The greatest number is ->" , num3)

#check the number is multiple of 7 or not
# num = int(input("Enter the number: "))
# if(num % 7 == 0):
#     print("The number is multiple of 7")
# else:
#     print("The number is not multiple of 7")

#find greatest out of 4 numbers
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# num4 = int(input("Enter the fourth number: "))
# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print("The greatest number is ->" , num1)
# elif(num2 > num3 and num2 > num4):
#     print("The greatest number is ->" , num2)
# elif(num3 > num4):
#     print("The greatest number is ->" , num3)
# else:
#     print("The greatest number is ->" , num4)
